## Links:

### Question: Why is there a sudden drop on Spark performance??
![graph4](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/88r.jpg)



### Is Memory Size the Bottleneck of Spark Performance? Yes and No

>cached datasets that do not fit in memory are either spilled to disk or recomputed on the fly when needed, as determined by the RDD's storage level. 

[From: Does my data need to fit in memory to use Spark?](https://spark.apache.org/faq.html)

	

### An Interesting Fact from Another Benchmarking Paper...
![graph1](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/89r.jpg)
![graph2](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/90r.jpg)
[From: PERFORMANCE COMPARISON BY RUNNING BENCHMARKS ONHADOOP, SPARK, AND HAMR](https://udspace.udel.edu/bitstream/handle/19716/17628/2015_LiuLu_MS.pdf)

### ...Which would make sense...

![graph3](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/91r.jpg)

From: My Hadoop Graphic UI
### ...True Reason: Insufficient RDDs, Redundant Computation and Best Use Case
![Benchmark Bar Graph](https://github.com/h4x0rMadness/Note/blob/master/EC528/Spark-demo/img/92r.jpg)

[From: my benchmark result](https://docs.google.com/presentation/d/1NgW_wVI9jGW7v0X-wA9BJ5P7Y8_vDF1GhuCA8n1NmFs/edit?ts=5e7bf721#slide=id.g720af4914c_2_113)


