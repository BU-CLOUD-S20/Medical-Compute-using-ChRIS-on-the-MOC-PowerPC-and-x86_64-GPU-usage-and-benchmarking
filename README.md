# Medical-Compute-using-ChRIS-on-the-MOC-PowerPC-and-x86_64-GPU-usage-and-benchmarking

## 0.   Contributors:

**Mentor**: Rudolph Pienaar (rudolphpienaar)

**Group Members**:

- Elizabeth Slade (https://github.com/emslade23)

- Shineun Yoon (https://github.com/ShineunYoon)

- Bowen Jia (https://github.com/jbw0410)

- Haoyang Wang (https://github.com/PupilTong)

- Kefan Zhang (https://github.com/h4x0rMadness)

## 0.   ChRIS Introduction:

- Red Hat "Creating ChRIS": https://www.redhat.com/en/creating-chris

- Boston University Red Hat Collaboratory of ChRIS : https://www.bu.edu/rhcollab/projects/radiology/

## 1.   Vision and Goals Of The Project:

The overall vision of the ChRIS project is to develop a plugin based on ChRIS platform so that users like developers or administrators are able to do benchmarking on cloud network topologies that include different architectures like x86 and PowerPC.

We are going to get familiar with Mass Open Cloud, ChRIS platform, ChRIS plugins and benchmarking methods in order to integrate all the components.

Our benchmarking plug-in will be the first ChRIS plug-in that can test performance of the ChRIS platform.


### High-level goals include:

- Improve the functions of our benchmarking ChRIS plugin 

- Use the real work environment to further improve the ChRIS plugin to better benchmark


## 2. Users/Personas Of The Project:

User Persona Examples:

- As a ChRIS developer / administrator, I would like to have a way to test how my plugin performs on different architectures such as x86 vs PowerPC therefore I want a ChRIS plugin that performs benchmarking tests on these architectures.

Non-target users are:

- Clinicians / Technicians / Patients who may use ChRIS platform but don't do or care about benchmarking between different architectures.



** **

## 3.   Scope and Features Of The Project:


We will focus on one plug-in which provides a series of tools and test functions to test the performance of the system. Based on what we decide is feasible, the test functions may range from a simple matrix multiplying to huge neural network training. These test functions will represent real workloads that may be deployed on the system. For example, if the real functions move data between main memory and GPU memory frequently, our functions are supposed to show this feature.


However, we are not focusing on building a precious and complex machine learning model or data processing method. All test functions will run fast and estimate the time that may be spent on running real computing tasks. These tests will run in an acceptable time span, like several minutes. Therefore, they should emulate the real ChRIS workloads as light as possible. Since there is no reason to run a benchmarking task for 8 hours rather than run a real task for 8 hours, we will ESTIMATE the performance.

At last, this plugin will produce comparable results that allow users to compare the performance of different platforms in an elegant and easy method.

## 4. Solution Concept

### Global Architectural Structure Of the Project:

This section provides a high-level architecture or a conceptual diagram showing the scope of the solution. If wireframes or visuals have already been done, this section could also be used to show how the intended solution will look. This section also provides a walkthrough explanation of the architectural structure.

## 5. Acceptance criteria

Correctly developed a runnable ChRIS plugin that to some extent presents the performance differences between different platform architectures.
The minimal product presents the benchmark differences between x86 and PowerPC.

## Our Plug-ins 

### Matrix Multiplication plugin

#### Docker Images

- [Matrix Multiply Plugin for x86_64 Architecture](https://hub.docker.com/repository/docker/fnndsc/pl-matrixmultiply_moc_x86_64)

- [Matrix Multiply Plugin for Power9 Architecture](https://hub.docker.com/repository/docker/fnndsc/pl-matrixmultiply_moc_ppc64)

#### Source code
- [Matrix_Multiply_x86_64 Source Code](https://github.com/FNNDSC/pl-matrixmultiply_moc_x86_64)

- [Matrix_Multiply_Power9 Source Code](https://github.com/FNNDSC/pl-matrixmultiply_moc_ppc64)

### Object Detection plugin

#### Docker image

- [Object Detection for x86 Architecture](https://hub.docker.com/repository/docker/fnndsc/pl-objectdetection_x86)

- [Object Detection for Power9 Archtecture](https://hub.docker.com/repository/docker/fnndsc/pl-objectdetection_moc_ppc64)

#### Source code

- [Object Detection x86 Source Code](https://github.com/FNNDSC/pl-objectdetection_x86)

- [Object Detection Power9 Source Code](https://github.com/FNNDSC/pl-objectdetection_moc_ppc64)

- [Object Detection Example Source Code](https://github.com/FNNDSC/objectdetection_example)

### Step 1: How to Build Our Docker Container

- For ppc64le image, we cannot use the automatic build on docker hub. We have to build this container locally and push it into docker hub.

```bash
    cd path/to/this/repo
    docker login docker.io -u [your docker.io username]
    docker build -f Dockerfile -t docker.io/fnndsc/pl-objectdetection_moc_ppc64 .
    docker push "docker.io/fnndsc/pl-objectdetection_moc_ppc64"

```

### Deploy requirement
- Your host computer should be a linux os and installed CUDA 10.1 && nvidia container.

	- For ppc64le machine: https://github.com/FNNDSC/pl-objectdetection_moc_ppc64

	- For x86_64 machine: https://github.com/FNNDSC/pl-objectdetection_x86

### Dependencies

	ffmpeg
	opencv-python
	tensorflow
	tensorrt

### Step 2: How to Run Our Containers

#### Using `docker run`

A. Check this repo for more information https://github.com/FNNDSC/objectdetection_example

B. To run using `docker`, be sure to assign an "input" directory to
`/incoming` and an output directory to `/outgoing`. *Make sure that the*
`$(pwd)/out` *directory is world writable!*
	- And use the `--f` flag to set the inputfile inside your `/incoming` directory.

C. Now, prefix all calls with

``` {.sourceCode .bash}
docker run --security-opt label=type:nvidia_container_t    \
           -v $(pwd):/incoming:z -v $(pwd)/out:/outgoing:z \
           docker.io/fnndsc/pl-matrixmultiply_moc_ppc64    \
           objectdetection.py                               \
           -f animal360p.webm /incoming /outgoing
```


### Concept: How our plugins work

*Get detailed information from: https://medium.com/better-programming/real-time-object-detection-on-gpus-in-10-minutes-6e8c9b857bb3*

*this image powered by previous url*

![workflow](https://miro.medium.com/max/1400/0*mnywPWQIQW5j0Paf)

This graph show the workflow of the original python script (provided by nVidia). One of the difference in our scripts is that we use a file instead of the web camera as graph source. Therefore, this container have to use the ffmpeg to decode the video file. Also, since there is no graphic interface in the server/moc/openshift, we removed the realtime progress showing codes and replace it by saving the output to an output file (output.avi) in the `outgoing` directiory. This means ffmpeg is essentical.

There is another output file called `FramePerSecondRecord.csv`. This file contains the benchmarking results of the plugin. The output should be like this:
```
maximum_fps,minimum_fps,average_fps
250.0,142.86,239.92
```
*(If you run it multiple times , the newest result will be added to the last line of file.)*

*(Result is gotten from a ppc64le machine)*

This shows the information about the inference time for every frame. We think it shows the data bus latency from cpu/main memory to the GPU.
### Benchmarking result.
On ppc64le machine, the typical inference time for each frame is about 4 ms. However in x86_64 machine, we got about 6~7 ms inference time for every frame. We think the differnece is significant (powerpc is about 40% faster than x86_64).
### Troubleshoot

#### Possible error 1: Error opening video stream or file

This means the opencv didn't open the video file successfully. Check:

* If the file exist
* If the input video coding format is supported by curent version ffmpeg.

##### Possible error 2: Failed to establish a new connection

Please contact the machine administrator to ensure the docker has the internet access ability.

### Design Implications and Discussion:

The goal for the ChRIS platform is to provide a containerized application that is made up of many plugins which run specific functions on inputs. The scope for our portion of the project is to develop one plugin that runs a function to benchmark performance between different architectures. The reason for this design is to make the plugin easy to use and integrate with a ChRIS developers workflow. 

The implications for our global architecture design are to allow ChRIS developers to use ChRIS to benchmark different architectures to find which one maximize their ChRIS plugin performance.



## 6.  Release Planning:

The release planning section describes how the project will deliver incremental sets of features and functions in a series of releases to completion. Identification of user stories associated with iterations that will ease/guide sprint planning sessions is encouraged. Higher-level details for the first iteration is expected.


### Sprint 1: February 12th, 2020
https://docs.google.com/presentation/d/1Q2wXZ6P_aQ-WBZZ00wB3yAEC8cJ0w2DTWR_6CjPHYpg/edit?usp=sharing

Get familiar with the ChRIS platform, either from web-app/ terminal operations.  
	
Set up environments for future development. (Linux/ docker)  

Research on how to use MOC(Mass Open Cloud)

Build a simple benchmarking programm and run it locally, e.g. Matrix-multiplying. 


### Sprint 2: February 26, 2020
https://docs.google.com/presentation/d/1VaiilM10SGllF1NvFY-7M7gkcGYEISwBvZEgpl1rioc/edit?usp=sharing

Research on a more complex benchmarking programm, e.g. 'Real-Time Object Detection on GPU'. 

Be able to run operations on the MOC computers

Be able to run plugins from the local ChRIS instance

### Sprint 3: March 7, 2020
https://docs.google.com/presentation/d/1j4j9gbuXU0PqSLAmS5srqlPlIC8HRmfBWQe3xtvopHM/edit?usp=sharing

Be able to run a pre-existent plugin via ChRIS on the MOC GPUs.

Develop benchmarking metrics to analyze plugin processes. 


### Sprint 4: March 19, 2020
https://docs.google.com/presentation/d/1NGK1S3wrcgw16NgElWnGRWkyDPuigEV01H0cjzWhFNg/edit?usp=sharing

Integrate our plugin into the ChRIS platform.

Get more granular with benchmarking metrics


### Sprint 5: April 2, 2020
https://docs.google.com/presentation/d/1YQ5Jg-ek9q0KNLdDgN3uF2i2k72bBYIeSLijLClmZnA/edit?usp=sharing



** **

## Lecture on Spark: April 6, 2020
https://docs.google.com/presentation/d/1NgW_wVI9jGW7v0X-wA9BJ5P7Y8_vDF1GhuCA8n1NmFs/edit?usp=sharing

Our team gave a class talk on Spark, which is a distributed computing framework designed for applications.

