import os
import ctypes
import time
import sys
import argparse
import csv

import cv2
import numpy as np
from PIL import Image
import tensorrt as trt

import utils.inference as inference_utils # TRT/TF inference wrappers
import utils.model as model_utils # UFF conversion
import utils.boxes as boxes_utils # Drawing bounding boxes
import utils.coco as coco_utils # COCO dataset descriptors
from utils.paths import PATHS # Path management

import pycuda.driver as cuda
import pycuda.autoinit

# COCO label list
COCO_LABELS = coco_utils.COCO_CLASSES_LIST

# Model used for inference
MODEL_NAME = 'ssd_inception_v2_coco_2017_11_17'

# Confidence threshold for drawing bounding box
VISUALIZATION_THRESHOLD = 0.5

# Precision command line argument -> TRT Engine datatype
TRT_PRECISION_TO_DATATYPE = {
    16: trt.DataType.HALF,
    32: trt.DataType.FLOAT,
    8: trt.DataType.INT8
}

# Layout of TensorRT network output metadata
TRT_PREDICTION_LAYOUT = {
    "image_id": 0,
    "label": 1,
    "confidence": 2,
    "xmin": 3,
    "ymin": 4,
    "xmax": 5,
    "ymax": 6
}


def fetch_prediction_field(field_name, detection_out, pred_start_idx):
    """Fetches prediction field from prediction byte array.

    After TensorRT inference, prediction data is saved in
    byte array and returned by object detection network.
    This byte array contains several pieces of data about
    prediction - we call one such piece a prediction field.
    The prediction fields layout is described in TRT_PREDICTION_LAYOUT.

    This function, given prediction byte array returned by network,
    staring index of given prediction and field name of interest,
    returns prediction field data corresponding to given arguments.

    Args:
        field_name (str): field of interest, one of keys of TRT_PREDICTION_LAYOUT
        detection_out (array): object detection network output
        pred_start_idx (int): start index of prediction of interest in detection_out

    Returns:
        Prediction field corresponding to given data.
    """
    return detection_out[pred_start_idx + TRT_PREDICTION_LAYOUT[field_name]]

def analyze_prediction(detection_out, pred_start_idx, img_pil):
    image_id = int(fetch_prediction_field("image_id", detection_out, pred_start_idx))
    label = int(fetch_prediction_field("label", detection_out, pred_start_idx))
    confidence = fetch_prediction_field("confidence", detection_out, pred_start_idx)
    xmin = fetch_prediction_field("xmin", detection_out, pred_start_idx)
    ymin = fetch_prediction_field("ymin", detection_out, pred_start_idx)
    xmax = fetch_prediction_field("xmax", detection_out, pred_start_idx)
    ymax = fetch_prediction_field("ymax", detection_out, pred_start_idx)
    if confidence > VISUALIZATION_THRESHOLD:
        class_name = COCO_LABELS[label]
        confidence_percentage = "{0:.0%}".format(confidence)
        print("Detected {} with confidence {}".format(
            class_name, confidence_percentage))
        boxes_utils.draw_bounding_boxes_on_image(
            img_pil, np.array([[ymin, xmin, ymax, xmax]]),
            display_str_list=["{}: {}".format(
                class_name, confidence_percentage)],
            color=coco_utils.COCO_COLORS[label]
        )

def parse_commandline_arguments():
    """Parses command line arguments and adjusts internal data structures."""

    # Define script command line arguments
    parser = argparse.ArgumentParser(description='Run object detection inference on input image.')
    parser.add_argument('--input_img_path', metavar='INPUT_IMG_PATH',
        help='an image file to run inference on')
    parser.add_argument('-p', '--precision', type=int, choices=[32, 16, 8], default=32,
        help='desired TensorRT float precision to build an engine with')
    parser.add_argument('-b', '--max_batch_size', type=int, default=1,
        help='max TensorRT engine batch size')
    parser.add_argument('-w', '--workspace_dir',
        help='sample workspace directory')
    parser.add_argument('-fc', '--flatten_concat',
        help='path of built FlattenConcat plugin')
    parser.add_argument('-d', '--calib_dataset', default='../VOCdevkit/VOC2007/JPEGImages',
        help='path to the calibration dataset')
    parser.add_argument('-c', '--camera', default=True,
        help='if True, will run webcam application')
    parser.add_argument('-op', '--outpath',
        help='output directory path')

    # Parse arguments passed
    args = parser.parse_args()

    # Set FlattenConcat TRT plugin path and
    # workspace dir path if passed by user
    if args.flatten_concat:
        PATHS.set_flatten_concat_plugin_path(args.flatten_concat)
    if args.workspace_dir:
        PATHS.set_workspace_dir_path(args.workspace_dir)

    try:
        os.makedirs(PATHS.get_workspace_dir_path())
    except:
        pass

    # Verify Paths after adjustments. This also exits script if verification fails
    PATHS.verify_all_paths()

    # Fetch TensorRT engine path and datatype
    args.trt_engine_datatype = TRT_PRECISION_TO_DATATYPE[args.precision]
    args.trt_engine_path = PATHS.get_engine_path(args.trt_engine_datatype,
        args.max_batch_size)
    try:
        os.makedirs(os.path.dirname(args.trt_engine_path))
    except:
        pass

    return args

def main(max_time, min_time, sum_time, num):

    # Parse command line arguments
    args = parse_commandline_arguments()
    outputdir_path = args.outpath
    # Fetch .uff model path, convert from .pb
    # if needed, using prepare_ssd_model
    ssd_model_uff_path = PATHS.get_model_uff_path(MODEL_NAME)
    if not os.path.exists(ssd_model_uff_path):
        model_utils.prepare_ssd_model(MODEL_NAME)

    # Set up all TensorRT data structures needed for inference
    trt_inference_wrapper = inference_utils.TRTInference(
        args.trt_engine_path, ssd_model_uff_path,
        trt_engine_datatype=args.trt_engine_datatype,
        calib_dataset = args.calib_dataset,
        batch_size=args.max_batch_size)
    ARGS = 3
    print("TRT ENGINE PATH", args.trt_engine_path)

    if args.camera == True:
    #if True:
        #print('Running webcam:', args.camera)
        # Define the video stream
        #cap = cv2.VideoCapture(0)
        #cap = cv2.VideoCapture('animal.webm')  # Change only if you have more than one webcams
        cap = cv2.VideoCapture(str(os.environ['APPROOT']) + '/objectdetection/animal360p.webm')  # Change only if you have more than one webcams
        if (cap.isOpened()== False):
            print("Error opening video stream or file")
            exit()
        else:
            print("success!")
        # Default resolutions of the frame are obtained.The default resolutions are system dependent.
	    # We convert the resolutions from float to integer.
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fps = cap.get(cv2.CAP_PROP_FPS)

	    # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
        out = cv2.VideoWriter('animal360pOutput.mp4',cv2.VideoWriter_fourcc(*'XVID'), fps, (frame_width,frame_height))

        # Loop for running inference on frames from the webcam
        while True:
            # Read frame from camera (and expand its dimensions to fit)
            ret, image_np = cap.read()
            if not ret:
                print("Video played.")
                break
            # Actually run inference
            cur, detection_out, keep_count_out = trt_inference_wrapper.infer_webcam(image_np)
            max_time = max(max_time, cur)
            min_time = min(min_time, cur)
            sum_time += cur
            num += 1

            # Overlay the bounding boxes on the image
            # let analyze_prediction() draw them based on model output
            img_pil = Image.fromarray(image_np)
            prediction_fields = len(TRT_PREDICTION_LAYOUT)
            for det in range(int(keep_count_out[0])):
                analyze_prediction(detection_out, det * prediction_fields, img_pil)
            final_img = np.asarray(img_pil)

            out.write(final_img)
        return outputdir_path, max_time, min_time, sum_time, num
            # Display output
            ## cv2.imshow('object detection', final_img)

            #if cv2.waitKey(25) & 0xFF == ord('q'):
            #    cap.release()
            #    out.release()
            #    cv2.destroyAllWindows()
            #    break
def createOrUpdate(outdir, data):
    headers = ["maximum_fps", "minimum_fps", "average_fps"]
    filepath = outdir  + '/FramePerSecondRecord.csv'
    # filepath = str(os.environ['APPROOT']) + '/FramePerSecondRecord.csv'
    print(filepath) ## -op/FramePerSecondRecord.csv
    if (os.path.exists(filepath)):
        # if the file exist add the value of the dictionary,else will build a new file with the header
        with open(filepath, 'a+') as f:

            f_csv = csv.DictWriter(f, headers)
            for item in data:
                f_csv.writerow(item)
    else:
        # %s/timestamp.json' % options.outputdir,
        with open(filepath, 'a+') as f:
            f_csv = csv.DictWriter(f, headers)
            # write headers to database.csv
            f_csv.writeheader()
            # write values of input Python Dictionary to database.csv row by row
            for item in data:
                f_csv.writerow(item)
if __name__ == '__main__':
    #outputdir = "/root/ec528-Chris-group/kefan/k3/pl-object-detection_moc_ppc64/SSD_Model"
    maxt = 0
    mint = 10000
    sumt = 0
    numf = 0
    outputdir, maxt, mint, sumt, numf = main(maxt, mint, sumt, numf)
    print("outputdir: "+str(outputdir))
    maxt /= 1000
    mint /= 1000
    sumt /= 1000
    max_fps = round(1 / mint, 2)
    min_fps = round(1 / maxt, 2)
    avg_fps = round(numf / sumt, 2)
    print("maximum_fps: " + str(max_fps) + "\n" + "minimum_fps: " + str(min_fps) + "\n" + "average_fps: " + str(avg_fps))
    data = [{'maximum_fps': max_fps, 'minimum_fps': min_fps, 'average_fps': avg_fps}]
    createOrUpdate(outputdir, data)


