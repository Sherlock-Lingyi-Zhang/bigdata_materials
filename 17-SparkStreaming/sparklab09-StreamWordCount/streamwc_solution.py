import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":  
    # launch this spark application by running:
    # > unset PYSPARK_DRIVER_PYTHON
    # > spark-submit --master local[2] streamwc.py
    sc = SparkContext(appName="Streaming WordCount")
    ssc = StreamingContext(sc, 1)
    
    # suppress INFO and WARN logs
    log4j = sc._jvm.org.apache.log4j
    log4j.LogManager.getRootLogger().setLevel(log4j.Level.ERROR)

    # Create a DStream that will connect to localhost:9999
    lines = ssc.socketTextStream("localhost", 9999)

    # transform the DStream to print the word count of each RDD in DStream
    lines.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda x, y: x + y) \
        .pprint()

    # Start the computation     
    ssc.start()             
    # Wait for the computation to terminate
    ssc.awaitTermination()  

