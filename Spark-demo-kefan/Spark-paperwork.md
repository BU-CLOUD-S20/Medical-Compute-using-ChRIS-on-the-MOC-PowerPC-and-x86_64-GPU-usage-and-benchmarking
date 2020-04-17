- What is Spark?

    Spark is an open-source cluster computing framework.

- What problems does Spark solve?

    For some applications that reuse a working set of data across multiple parallel operations, Spark provides higher efficiency, less latency and also same fault-tolerence and scalability as MapReduce.

    ![image-20200327150712793](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327150712793.png)

    ![image-20200327150831018](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327150831018.png)

- How does it solve 'em?

    

- What's the impact of Spark?

- What's the comparison between Spark vs MapReduce?

- What's the drawback / summary of Spark?

    

- *Demo?





Data is too big to be processed on a single machine -> always hit the bottleneck

Hadoop:

	- HDFS: Distributed Storage
	- MapReduce: Computing Framework
	- YARN: Resource Manager



However, developers suffer from the performance.



Apache Spark -> x100 times faster than MapReduce



"Apache Spark is a fast and general purpose engine for large-scale data processing, it works on a cluster of computers."



which means:

1. A cluster computing engine
2. A set of libs, APIs and so on



![image-20200327141554142](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327141554142.png)

Apache Spark ecosystem

![image-20200327141708398](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327141708398.png)

Apache Spark doesn't have Cluster Resource Manager and Distributed Storage, but you can plug in to support them.

![image-20200327141812095](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327141812095.png)

it has Compute Engine that does memory management, task scheduling, fault recovery and interaction with cluster manager.

![image-20200327142005787](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327142005787.png)



Outside Spark Core, you have libs support other functions and languages.



## Why Spark?

1. Abstrct the parallel programming
2. Unified Platform
3. Ease of Use



### how do we execute programs on a Spark Cluster?

1. Interactive Clients (Scala shell, Python shell, jupyter notebooks) for exploration
2. Submit a job (Spark submit utility) for executing a production application

### how does the Spark execute our programs on a cluster?

![image-20200327144529092](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327144529092.png)



(**Demo: Run spark example to calculate pi locally and on google cluster**)



Spark application flow:

![image-20200327145419747](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327145419747.png)



### RDD:

Spark RDD is a ***resilient, partitioned, distributed and immutable*** (read only) collection of data



![image-20200327145627820](/Users/robertmorrislike/Library/Application Support/typora-user-images/image-20200327145627820.png)



### how to create a RDD:

1. load some data from a source
2. create a RDD by transforming another RDD



(**Demo: load RDD**)



