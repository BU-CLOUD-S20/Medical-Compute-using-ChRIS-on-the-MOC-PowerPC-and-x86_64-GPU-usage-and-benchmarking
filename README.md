# Medical-Compute-using-ChRIS-on-the-MOC-PowerPC-and-x86_64-GPU-usage-and-benchmarking

## Introduction to ChRIS

- [Red Hat "Creating ChRIS"](https://www.redhat.com/en/creating-chris)

- [Boston University Red Hat Collaboratory of ChRIS](https://www.bu.edu/rhcollab/projects/radiology/)

## Table of Content
[1.   Vision and Goals Of The Project](#1---vision-and-goals-of-the-project)<br/>
[2.   Users/Personas Of The Project](#t3)<br/>
[3.   Scope and Features Of The Project](#3---scope-and-features-of-the-project)<br/>
[4.   Solution Concept](#4---solution-concept)<br/>
[5.   Acceptance criteria](#5---acceptance-criteria)<br/>
[6.   Release Planning](#6---release-planning)<br/>

### [Final Project Demonstration](https://www.youtube.com/watch?v=1e_rx_YLQEw)
[![Final Project Demonstration](https://img.youtube.com/vi/1e_rx_YLQEw/0.jpg)](https://youtu.be/1e_rx_YLQEw)

### [Product Documentation](#product-documentation)
- [I. Matrix Multiplication Plugin](#i-matrix-multiplication-plugin)
  * [Description](#description)
  * [Usage](#usage)
  * [Example](#example)
- [II. Object Detection Plugin](#ii-object-detection-plugin)
  * [Description](#description-1)
  * [Usage](#usage-1)
  * [Example](#example-1)
  
### [ChRIS Workflow Documentation](#chris-workflow-documentation)
- [ChRIS Plugin Workflow on Titan](#chris-plugin-workflow-on-titan)
- [Running `pman` and `pfioh` on Power9 Cluster in the Mass Open Cloud](#t8)
    
## Contributors

**Mentor**: Rudolph Pienaar (rudolphpienaar)

**Group Members**:

- [Elizabeth Slade](https://github.com/emslade23)
- [Shineun Yoon](https://github.com/ShineunYoon)
- [Bowen Jia](https://github.com/jbw0410)
- [Haoyang Wang](https://github.com/PupilTong)
- [Kefan Zhang](https://github.com/h4x0rMadness)

** **
<a name="t2"></a>
## 1.   Vision and Goals Of The Project

The overall vision of the ChRIS project is to develop a plugin based on ChRIS platform so that users like developers or administrators are able to do benchmarking on cloud network topologies that include different architectures like x86 and PowerPC.

We are going to get familiar with Mass Open Cloud, ChRIS platform, ChRIS plugins and benchmarking methods in order to integrate all the components.

Our benchmarking plug-in will be the first ChRIS plug-in that can test performance of the ChRIS platform.


### High-level goals include:

- Improve the functions of our benchmarking ChRIS plugin 

- Use the real work environment to further improve the ChRIS plugin to better benchmark


<a name="t3"></a>
## 2.   Users/Personas Of The Project

- User Persona Examples:

As a ChRIS developer / administrator, I would like to have a way to test how my plugin performs on different architectures such as x86 vs PowerPC therefore I want a ChRIS plugin that performs benchmarking tests on these architectures.

- Non-target users are:

Clinicians / Technicians / Patients who may use ChRIS platform but don't do or care about benchmarking between different architectures.


<a name="t4"></a>
## 3.   Scope and Features Of The Project


We will focus on one plug-in which provides a series of tools and test functions to test the performance of the system. Based on what we decide is feasible, the test functions may range from a simple matrix multiplying to huge neural network training. These test functions will represent real workloads that may be deployed on the system. For example, if the real functions move data between main memory and GPU memory frequently, our functions are supposed to show this feature.


However, we are not focusing on building a precious and complex machine learning model or data processing method. All test functions will run fast and estimate the time that may be spent on running real computing tasks. These tests will run in an acceptable time span, like several minutes. Therefore, they should emulate the real ChRIS workloads as light as possible. Since there is no reason to run a benchmarking task for 8 hours rather than run a real task for 8 hours, we will ESTIMATE the performance.

At last, this plugin will produce comparable results that allow users to compare the performance of different platforms in an elegant and easy method.

<a name="t5"></a>
## 4.   Solution Concept

### Global Architectural Structure Of the Project:

This section provides a high-level architecture or a conceptual diagram showing the scope of the solution. If wireframes or visuals have already been done, this section could also be used to show how the intended solution will look. This section also provides a walkthrough explanation of the architectural structure.

<a name="t6"></a>
## 5.   Acceptance criteria

Correctly developed a runnable ChRIS plugin that to some extent presents the performance differences between different platform architectures.
The minimal product presents the benchmark differences between x86 and PowerPC.

<a name="t7"></a>
## 6.   Release Planning

The release planning section describes how the project will deliver incremental sets of features and functions in a series of releases to completion. Identification of user stories associated with iterations that will ease/guide sprint planning sessions is encouraged. Higher-level details for the first iteration is expected.


### [Sprint 1: February 12th, 2020](https://docs.google.com/presentation/d/1Q2wXZ6P_aQ-WBZZ00wB3yAEC8cJ0w2DTWR_6CjPHYpg/edit?usp=sharing)

Get familiar with the ChRIS platform, either from web-app/ terminal operations.  
	
Set up environments for future development. (Linux/ docker)  

Research on how to use MOC(Mass Open Cloud)

Build a simple benchmarking programm and run it locally, e.g. Matrix-multiplying. 


### [Sprint 2: February 26, 2020](https://docs.google.com/presentation/d/1VaiilM10SGllF1NvFY-7M7gkcGYEISwBvZEgpl1rioc/edit?usp=sharing)

Research on a more complex benchmarking programm, e.g. 'Real-Time Object Detection on GPU'. 

Be able to run operations on the MOC computers

Be able to run plugins from the local ChRIS instance

### [Sprint 3: March 7, 2020](https://docs.google.com/presentation/d/1j4j9gbuXU0PqSLAmS5srqlPlIC8HRmfBWQe3xtvopHM/edit?usp=sharing)

Be able to run a pre-existent plugin via ChRIS on the MOC GPUs.

Develop benchmarking metrics to analyze plugin processes. 


### [Sprint 4: March 19, 2020](https://docs.google.com/presentation/d/1NGK1S3wrcgw16NgElWnGRWkyDPuigEV01H0cjzWhFNg/edit?usp=sharing)

Integrate our plugin into the ChRIS platform.

Get more granular with benchmarking metrics


### [Sprint 5: April 2, 2020](https://docs.google.com/presentation/d/1YQ5Jg-ek9q0KNLdDgN3uF2i2k72bBYIeSLijLClmZnA/edit?usp=sharing)

### [Final: May 4th, 2020](https://docs.google.com/presentation/d/1qJEkL9hwqAvVJLRmdV9ggfuaSdW3QREw2JFf2DviXn4/edit?usp=sharing)

** **

## [Lecture on Spark: April 6, 2020](https://docs.google.com/presentation/d/1NgW_wVI9jGW7v0X-wA9BJ5P7Y8_vDF1GhuCA8n1NmFs/edit?usp=sharing)

Our team gave a class talk on Spark, which is a distributed computing framework designed for applications.

** **

### Design Implications and Discussion:

The goal for the ChRIS platform is to provide a containerized application that is made up of many plugins which run specific functions on inputs. The scope for our portion of the project is to develop one plugin that runs a function to benchmark performance between different architectures. The reason for this design is to make the plugin easy to use and integrate with a ChRIS developers workflow. 

The implications for our global architecture design are to allow ChRIS developers to use ChRIS to benchmark different architectures to find which one maximize their ChRIS plugin performance.


** **
# Product Documentation

## I. Matrix Multiplication Plugin

#### Docker Images

- [Matrix Multiply Plugin for x86_64 Architecture](https://hub.docker.com/repository/docker/fnndsc/pl-matrixmultiply_moc_x86_64)

- [Matrix Multiply Plugin for Power9 Architecture](https://hub.docker.com/repository/docker/fnndsc/pl-matrixmultiply_moc_ppc64)

#### Source code
- [Matrix_Multiply_x86_64 Source Code](https://github.com/FNNDSC/pl-matrixmultiply_moc_x86_64)

- [Matrix_Multiply_Power9 Source Code](https://github.com/FNNDSC/pl-matrixmultiply_moc_ppc64)


Description
------------
```

                                 _        _                      _ _   _       _       
                                | |      (_)                    | | | (_)     | |      
                 _ __ ___   __ _| |_ _ __ ___  ___ __ ___  _   _| | |_ _ _ __ | |_   _ 
                | '_ ` _ \ / _` | __| '__| \ \/ / '_ ` _ \| | | | | __| | '_ \| | | | |
                | | | | | | (_| | |_| |  | |>  <| | | | | | |_| | | |_| | |_) | | |_| |
                |_| |_| |_|\__,_|\__|_|  |_/_/\_\_| |_| |_|\__,_|_|\__|_| .__/|_|\__, |
                                                                        | |       __/ |
                                                                        |_|      |___/ 
```

This is a benchmarking plugin for ChRIS platform of Boston Children's Hospital ([What is ChRIS?](https://www.bu.edu/rhcollab/projects/radiology/))on both x86_64 and PowerPC MOC using matrix multiplication.
| Plugin Info  | Content | Description |
|:------------:|:-----------------:|:-------------------------------------------------------------:|
| Input | matrix parameters | COE value to indicate matrix size, given by command line |
| Output | one .csv file | Contains matrix size and running time for multiplication task |


Usage
-------------------
### Requirements
Your host computer should be a linux os and installed CUDA 10.1 && nvidia container.



### Docker run on x86_64

First pull docker image to local environment:
```
docker pull fnndsc/pl-matrixmultiply_moc_x86_64
```
Then you can run it with parameters:
``` {.sourceCode .bash}
docker run --runtime=nvidia                                         \
            -e NVIDIA_VISIBLE_DEVICES=1                             \
            -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing          \
            fnndsc/pl-matrixmultiply                                \
            matmultiply.py                                          \
            -c 32,32,128                                            \
            /incoming /outgoing
```
Parameters and meaning below in the table:

| **docker run parameters for x86_64** |  |  |
|:--------------------------------:|:-----------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------:|
| **parameters** | **function** | **example** |
| --runtime=nvidia | tells the docker to use the nvidia docker | --runtime=nvidia |
| -e | specifies the visible graphic device id | -e NVIDIA_VISIBLE_DEVICES=1 |
| -v | specify input and outgoing folder, check docker [volume bind](https://docs.docker.com/storage/bind-mounts/) | -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing |
| image_name | specify docker image name | fnndsc/pl-matrixmultiply |
| script_name | specify script file to run | matmultiply.py                                           |
| -c | specify COE value to define matrix size, format like: start_value, gap_value, end_value | -c 32,32,128 |

### Docker run on PowerPC
First pull docker image to local environment:
```
docker pull fnndsc/pl-matrixmultiply_moc_ppc64
```
Then you can run it with parameters:
``` {.sourceCode .bash}
docker run  --security-opt label=type:nvidia_container_t            \
            -v $(pwd):/incoming:z -v $(pwd)/out:/outgoing:z         \
            fnndsc/pl-matrixmultiply_moc_ppc64                      \
            matmultiply.py                                          \
            -c 32,32,128                                            \
            /incoming /outgoing
```
Parameters and meaning below in the table:


| **docker run parameters for PowerPC** |  |  |
|:--------------------------------------------:|:-----------------------------------------------------------------------------------------------------------:|:-----------------------------------------------:|
| **parameters** | **function** | **example** |
| --security-opt label=type:nvidia_container_t | tells the docker to use the nvidia docker | --security-opt label=type:nvidia_container_t |
| -v | specify input and outgoing folder, check docker [volume bind](https://docs.docker.com/storage/bind-mounts/) | -v $(pwd):/incoming:z -v $(pwd)/out:/outgoing:z |
| image_name | specify docker image name | fnndsc/pl-matrixmultiply_moc_ppc64 |
| script_name | specify script file to run | matmultiply.py |
| -c | specify COE value to define matrix size, format like: start_value, gap_value, end_value | -c 32,32,128 |

**Build Instructions**

For ppc64le image, we cannot use the automatic build on docker hub. We have to build this conatiner locally and push it into docker hub.

```bash
cd path/to/this/repo
docker login docker.io -u [your docker.io username]
docker build -f Dockerfile -t docker.io/fnndsc/pl-matrixmultiply_moc_ppc64 
docker push "docker.io/fnndsc/pl-matrixmultiply_moc_ppc64"

```
Example
-------

**x86_64**
``` {.sourceCode .bash}
docker run --runtime=nvidia                                         \
            -e NVIDIA_VISIBLE_DEVICES=1                             \
            -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing          \
            fnndsc/pl-matrixmultiply                                \
            matmultiply.py                                          \
            -c 32,32,128                                            \
            /incoming /outgoing
```

**PowerPC**
``` {.sourceCode .bash}
docker run  --security-opt label=type:nvidia_container_t            \
            -v $(pwd):/incoming:z -v $(pwd)/out:/outgoing:z         \
            fnndsc/pl-matrixmultiply_moc_ppc64                      \
            matmultiply.py                                          \
            -c 32,32,128                                            \
            /incoming /outgoing
```

Research and Development References
-------------

### Workflow

What this plugin simply does is, when assigned with the COE parameter (`-c`), it will generate a list of COE values, for example, `-c 32,32,128` will generate four parameters of COE as: `[32, 64, 96, 128]`, and it is not necessary to assign the end value as exactly divisible by gap value. (which means you can go with `-c 32,32,100`.

For each COE value in this list, it will generate square matrix with size to be `(COE x TPB) ^2`, where `TPB` value is determined as 32 in the program, and therefore you have different sizes of matrix to do multiplication.

The program will record this running time along with start time, end time and matrix size, and generate a `.csv` file in your output folder, that's what you can use for benchmarking purpose.



Troubleshoot
-------

Make sure your `/out` directory has corresponding authorization, you can try:

```
mkdir in out && chmod 777 out                                       
```


Related Links
----------
https://medium.com/datathings/benchmarking-blas-libraries-b57fb1c6dc7

## II. Object Detection Plugin

#### Docker image

- [Object Detection for x86 Architecture](https://hub.docker.com/repository/docker/fnndsc/pl-objectdetection_x86)

- [Object Detection for Power9 Archtecture](https://hub.docker.com/repository/docker/fnndsc/pl-objectdetection_moc_ppc64)

#### Source code

- [Object Detection x86 Source Code](https://github.com/FNNDSC/pl-objectdetection_x86)

- [Object Detection Power9 Source Code](https://github.com/FNNDSC/pl-objectdetection_moc_ppc64)

- [Object Detection Example Source Code](https://github.com/FNNDSC/objectdetection_example)

  
Description
------------
```
                  ___  _     _           _     ____       _            _   _             
                 / _ \| |__ (_) ___  ___| |_  |  _ \  ___| |_ ___  ___| |_(_) ___  _ __  
                | | | | '_ \| |/ _ \/ __| __| | | | |/ _ \ __/ _ \/ __| __| |/ _ \| '_ \ 
                | |_| | |_) | |  __/ (__| |_  | |_| |  __/ ||  __/ (__| |_| | (_) | | | |
                 \___/|_.__// |\___|\___|\__| |____/ \___|\__\___|\___|\__|_|\___/|_| |_|
                          |__/                                                           


```

This is a GPU benchmarking plugin for ChRIS platform of Boston Children's Hospital ([What is ChRIS?](https://www.bu.edu/rhcollab/projects/radiology/))on both x86_64 and PowerPC MOC using object detection.

|Plugin Info  | Content | Description |
|:------:|:--------------:|:-----------------------------------------------:|
| Input | one video file | Target file to be tested with object detection |
| Output | one .csv file | Contains test results maximum frame per second, minimum frame per second and average frame per second  |



Usage
-------------------
### Requirements
Your host computer should be a linux os and installed CUDA 10.1 && nvidia container.

Main Dependencies:
`ffmpeg`
`opencv-python`
`tensorflow`
`tensorrt`

### Docker run on x86_64

First pull docker image to local environment:
```
docker pull docker.io/fnndsc/pl-objectdetection_x86
```
Then you can run it with parameters:
``` {.sourceCode .bash}
docker run --runtime=nvidia                                         \
            -e NVIDIA_VISIBLE_DEVICES=1                             \
            -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing          \
            docker.io/fnndsc/pl-objectdetection_x86                 \
            objectdetection.py                                      \
            -f animal360p.webm                                      \
            /incoming /outgoing
```
Parameters and meaning below in the table:

| **docker run parameters for x86_64**       |  |  |
|-----------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| **parameters** | **function** | **example** |
| --runtime=nvidia | tells the docker to use the nvidia docker | --runtime=nvidia |
| -e | specifies the visible graphic device id | -e NVIDIA_VISIBLE_DEVICES=1 |
| -v | specify input and outgoing folder, check docker [volume bind](https://docs.docker.com/storage/bind-mounts/) | -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing |
| image_name | specify docker image name | docker.io/fnndsc/pl-objectdetection_x86 |
| script_name | specify script file to run | objectdetection.py |
| -f, --file | specify input file for object detection in input folder | -f animal360p.webm |

### Docker run on PowerPC
First pull docker image to local environment:
```
docker pull docker.io/fnndsc/docker.io/fnndsc/pl-objectdetection_moc_ppc64
```
Then you can run it with parameters:
``` {.sourceCode .bash}
docker run --security-opt label=type:nvidia_container_t     \
           -v $(pwd):/incoming:z -v $(pwd)/out:/outgoing:z  \
           docker.io/fnndsc/pl-objectdetection_moc_ppc64     \
           objectdetection.py                               \
           -f animal360p.webm                               \
           /incoming /outgoing
```
Parameters and meaning below in the table:


| **docker run parameters for PowerPC** |  |  |
|----------------------------------------------|-------------------------------------------------------------|-------------------------------------------------|
| **parameters** | **function** | **example** |
| --security-opt label=type:nvidia_container_t | tells the docker to use the nvidia docker | --security-opt label=type:nvidia_container_t |
| -v | specify input and outgoing folder, check docker [volume bind](https://docs.docker.com/storage/bind-mounts/) | -v $(pwd):/incoming:z -v $(pwd)/out:/outgoing:z |
| image_name | specify docker image name |            docker.io/fnndsc/pl-matrixmultiply_moc_ppc64     |
| script_name | specify script file to run | objectdetection.py |
| -f, --file | specify input file for object detection in input folder | -f animal360p.webm |

**Build Instructions**

For ppc64le image, we cannot use the automatic build on docker hub. We have to build this conatiner locally and push it into docker hub.

```bash
cd path/to/this/repo
docker login docker.io -u [your docker.io username]
docker build -f Dockerfile -t docker.io/fnndsc/pl-objectdetection_moc_ppc64 .
docker push "docker.io/fnndsc/pl-objectdetection_moc_ppc64"

```
Example
-------
For both `x86_64` and `PowerPC`, please check `FNNDSC/objectdetection_example` repo for example usage:[objectdetection_example](https://github.com/FNNDSC/objectdetection_example)

Research and Development References
-------------

### Workflow

![workflow](https://miro.medium.com/max/1400/0*mnywPWQIQW5j0Paf)


This graph show the workflow of the original python script (provided by nVidia). One of the difference in our scripts is that we use a file instead of the web camera as graph source. Therefore, this container have to use the ffmpeg to decode the video file. Also, since there is no graphic interface in the server/moc/openshift, we removed the realtime progress showing codes and replace it by saving the output to an output file (output.avi) in the `outgoing` directiory. This means ffmpeg is essentical.

There is another output file called `FramePerSecondRecord.csv`. This file contains the benchmarking results of the plugin. The output should be like this:
| maximum_fps  | minimum_fps | average_fps |
|:------------:|:-----------:|:-----------:|
|                                                                                                                            250.0                                                                                                                          |                                                                     142.86                                                                    |                                                                                                                      239.92                                                                                                                    |

If you wanna more research details of this project, [check this tutorial.](https://medium.com/better-programming/real-time-object-detection-on-gpus-in-10-minutes-6e8c9b857bb3)


(If you run it multiple times , the newest result will be added to the last line of file.)

(Results from a `ppc64le` machine)

This shows the information about the inference time for every frame. We think it shows the data bus latency from cpu/main memory to the GPU.

### Benchmarking result
On `ppc64le` machine, the typical inference time for each frame is about 4 ms. However in `x86_64` machine, we got about 6~7 ms inference time for every frame. We think the difference is significant (powerpc is about 40% faster than `x86_64`).


Troubleshoot
-------

#### Error opening video stream or file

This means the opencv didn't open the video file successfully. Check:

* If the file exist
* If the input video coding format is supported by curent version ffmpeg.

#### Failed to establish a new connection

Please contact the machine administrator to ensure the docker has the internet access ability.

Related Links
----------
Most python scripts in this repo is forked from this tensorRT example provided by Nvidia:

https://github.com/NVIDIA/object-detection-tensorrt-example

## ChRIS Workflow Documentation

## ChRIS Plugin Workflow on Titan
[ChRIS Plugin Workflow on Titan](https://github.com/BU-CLOUD-S20/Medical-Compute-using-ChRIS-on-the-MOC-PowerPC-and-x86_64-GPU-usage-and-benchmarking/blob/master/titan)

<a name="t8"></a>

## Running `pman` and `pfioh` on Power9 Cluster in the Mass Open Cloud

[`pman` ppc64le](https://hub.docker.com/repository/docker/emslade/pman.ppc64le)
[`pfioh` ppc64le](https://hub.docker.com/repository/docker/emslade/pfioh.ppc64le)

#### If you want to pull the docker container

	docker pull docker.io/emslade/pman.ppc64le
	docker pull docker.io/emslade/pfioh.ppc64le

### Step 1: Log in to [Power9 Openshift](https://p9-openshift.osh.massopen.cloud:8443/)

### Step 2: Navigate to your project. Here you will see a "Add to Project" option in the top right hand corner.

### Step 3: Click on Add to Project -> Deploy Image

### Step 4: Now, check on Image Name. 

- if you want to deploy `pfioh`, include **emslade/pfioh.ppc64le** in the text box
- if you want to deploy `pman`, include **emslade/pman.ppc64le** in the text box
		
### Step 5: Then, click **Deploy** !

### Step 6: After `pman` and `pfioh` are deployed, you can say hello to these services. 
- Reference the [**pfcon wiki**](https://github.com/FNNDSC/pfcon/wiki/pfcon-*FS*-and-*DS*-plugin-example-on-moc-ppc64le-direct). 
Specifically, reference the [pfcon OpenShift ppc64le section](https://github.com/FNNDSC/pfcon/wiki/Running-plugins-on-the-MOC-(ppc64le-OpenShift))





