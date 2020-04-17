## Building Log of Spark Demo

### Local Mode + Submit Application

- Step 1: Installing JVM, Scala, Spark.

![img](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/1.png)

We see the Spark Web UI as well in the given url: http://1nspire:4040/jobs/

![img](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/2.png)

Task Dashboard:

![img](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/3.png)

- Step 2: Run Spark Examples

Try to run the spark pi calculation example, but somehow the spark folder we downloaded, we don't have the pi example.

Okay now problem fixed.

Running pi calculation example locally, with submit application mode.

With this command:
![img](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/5.png)

```
spark-submit --class org.apache.spark.examples.SparkPi /Users/robertmorrislike/LocalFilePath/EC528/Spark/spark-2.4.5-bin-hadoop2.7/examples/jars/spark-examples_2.11-2.4.5.jar 1000
```

Where 1000 is the ***numSlices*** parameter to denote the number of partitions the data would be parallelized to in the main class.

**numSlices parameter is for number of partitions of the program, but I think for this pi calculation program it really makes no influence since the data is just two random number in order to approximate pi and all it does with partition is to make it runs longer time so that we see the web UI, but mainly it's for huge data to be partitioned and processed, e.g. word count.**

We can see the progress on the dashboard:

![img](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/4.png)

And after paralleled computation finished, we get the result:

![img](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/6.png)

### Local Mode + Interactive Mode:

### \*Google Cloud Platform + Cluster:
