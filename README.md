# Medical-Compute-using-ChRIS-on-the-MOC-PowerPC-and-x86_64-GPU-usage-and-benchmarking

## 1.   Vision and Goals Of The Project:

Develop a Machine Learning/ Neural Network containerized application (or any other appropriate test application) plugin for the ChRIS platform as a sample application that could show the performance differences between different machine architectures.

** High-level goals include:**
Develop a sample test ChRIS plugin for benchmarking purposes.
Improve and extend the test applications on ChRIS in order to simulate a more similar working environment.
Improve the benchmarking ChRIS plugin code in order to extend the portability for all platforms.

## 2. Users/Personas Of The Project:

User Persona Examples:
Clinicians/Technicians want software that is easy to use, informative when helping them make a diagnosis and computes quick results so that they can maximize their time with their patients and make more informed decisions. 
Researchers want an open-source environment with accessible documentation, efficient computational resources, and useful plug-ins so that they can conduct efficient experiments on medical data

Non-target users are:
Clinicians/Technicians who don’t use MOC, ChRIS.
Users do not use PowerPC and x86_64 as their architecture


** **

## 3.   Scope and Features Of The Project:

We will focus on one node which provides a series of tools and test functions to test the performance of the system. The test functions may cover from a simple matrix multiplying to a huge neural network training, to represent the real workloads that may be deployed on the system. For example, if the real functions move data between main memory and GPU memory frequently, our functions are supposed to show this feature.


However, we are not focusing on building a precious and complex machine learning model or data processing method. All test functions will run fast, estimating time may spend on running real computing tasks in an acceptable time span, like several minutes. Therefore, they should emulate the real ChRIS workloads as light as possible. Since there is no reason to run a benchmark for 8 hours rather than run a real task for 8 hours to ESTIMATE the performance.

At last, this node will produce comparable results that allow users to compare the performance of different platforms in an elegant and easy method.

## 4. Solution Concept

This section provides a high-level outline of the solution.

Global Architectural Structure Of the Project:

This section provides a high-level architecture or a conceptual diagram showing the scope of the solution. If wireframes or visuals have already been done, this section could also be used to show how the intended solution will look. This section also provides a walkthrough explanation of the architectural structure.

<center><img src="./diagram001.png" width=75% display=block></img></center>

Design Implications and Discussion:

This section discusses the implications and reasons for the design decisions made during the global architecture design.

## 5. Acceptance criteria

Correctly developed a runnable ChRIS plugin that to some extent presents the performance difference between different platform architectures.
The minimal product presents the benchmark differences between x86 and PowerPC.


## 6.  Release Planning:

The release planning section describes how the project will deliver incremental sets of features and functions in a series of releases to completion. Identification of user stories associated with iterations that will ease/guide sprint planning sessions is encouraged. Higher-level details for the first iteration is expected.

Sprint 1: February 12th, 2020
	Get familiar with the ChRIS platform, either from web-app/ terminal operations.  
Set up environments for future development. (Linux/ docker)  
	Research on how to use MOC(Mass Open Cloud)
	Get the NIST dataset and research on training the ML model. 


** **

## General comments


