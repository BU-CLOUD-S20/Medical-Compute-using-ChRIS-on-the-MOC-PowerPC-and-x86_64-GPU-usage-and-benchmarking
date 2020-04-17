## Idea so far: Compare Spark vs MapReduce on same task 

- Initialize instances on Google Cloud Platform

- Visualize Web UI page locally (from **Connecting to a web interface** on GCP)
  ```
   gcloud compute ssh spark-m \
    --project=spark-demo-273003 \
    --zone=us-central1-b -- -D 1080 -N
  ```
  and on different terminal
  ```
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --proxy-server="socks5://localhost:1080" \
    --user-data-dir="/tmp/spark-m" http://spark-m:8088  
  ```
  
- Submit a Spark task in master node
  ```
  spark-submit --class org.apache.spark.examples.SparkPi --deploy-mode cluster file:///usr/lib/spark/examples/jars/spark-examples.jar 1000
  ```
  
  *not runnable*
  ```
  spark-submit --class org.apache.spark.examples.mllib.DenseKMeans --deploy-mode cluster file:///usr/lib/spark/examples     /jars/spark-examples.jar 1000 
  ```


- Hadoop Using Command line （deprecated)
  ```
  yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar pi 2 5 (map reduce parameter is not correct)
  ```

- Intel HiBench:

  kmeans
   ``` 
    bin/workloads/ml/kmeans/prepare/prepare.sh 
    bin/workloads/ml/kmeans/hadoop/run.sh 
    bin/workloads/ml/kmeans/spark/run.sh 
    
    cat hibench.report | column -t  

   ```
   
   
   ```
    Type              Date        Time      Input_data_size  Duration(s)  Throughput(bytes/s)  Throughput/node
    ScalaSparkKmeans  2020-04-03  20:20:52  1396212          30.391       45941                45941
    HadoopKmeans      2020-04-03  20:25:48  1396212          238.079      5864                 5864
    ScalaSparkKmeans  2020-04-03  20:35:18  602462544        53.126       11340257             11340257
    HadoopKmeans      2020-04-03  20:42:36  602462544        387.159      1556111              1556111
    ScalaSparkKmeans  2020-04-03  21:04:29  4016371638       777.511      5165678              5165678
    HadoopKmeans      2020-04-03  21:28:03  4016371638       1369.341     2933069              2933069
    ScalaSparkKmeans  2020-04-03  23:05:45  20081826151      5296.090     3791821              3791821
    HadoopKmeans      2020-04-04  00:59:24  20081826151      6306.330     3184391              3184391
   ```
## References:


