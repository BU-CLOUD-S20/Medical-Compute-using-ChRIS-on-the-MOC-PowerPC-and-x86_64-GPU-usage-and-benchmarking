import matplotlib.pyplot as plt
import tensorflow as tf
import time
import numpy as np

def get_times(maximum_time):

    device_times = {
        "/gpu:0":[],
        "/cpu:0":[]
    }
    matrix_sizes = range(500,50000,500)
    numpy_time =[]
    for size in matrix_sizes:
        print("####### Calculating, matrix size = ", size )
        x1 = np.random.random_sample((size, size))
        x2 = np.random.random_sample((size, size))
        start_time = time.time()
        result = np.dot(x1,x2)
        time_taken = time.time() - start_time
        numpy_time.append(time_taken)
        for device_name in device_times.keys():

            #print("####### Calculating on the " + device_name + " #######")

            shape = (size,size)
            data_type = tf.float32
            with tf.device(device_name):
                r1 = tf.random_uniform(shape=shape, minval=0, maxval=1, dtype=data_type)
                r2 = tf.random_uniform(shape=shape, minval=0, maxval=1, dtype=data_type)
                dot_operation = tf.matmul(r2, r1)


            with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as session:
                    start_time = time.time()
                    result = session.run(dot_operation)
                    time_taken = time.time() - start_time
                    #print(result)
                    device_times[device_name].append(time_taken)

            #print(device_times)

            if time_taken > maximum_time:
                device_times["native_numpy"] = numpy_time
                return device_times, matrix_sizes


device_times, matrix_sizes = get_times(10)
gpu_times = device_times["/gpu:0"]
cpu_times = device_times["/cpu:0"]
np_times  = device_times["native_numpy"]

plt.plot(matrix_sizes[:len(gpu_times)], gpu_times,'ro-', label="tensorflow on gpu")
plt.plot(matrix_sizes[:len(cpu_times)], cpu_times,'bx-',label="tensorflow on cpu")
plt.plot(matrix_sizes[:len(np_times)], np_times,'gs-',label="native numpy")
plt.ylabel('Time')
plt.xlabel('Matrix size')
plt.legend(loc='upper left')
plt.show()