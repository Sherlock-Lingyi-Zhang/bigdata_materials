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

    # todo: Create a DStream that will connect to localhost:9999
    

    # todo: transform the DStream to print the word count of each RDD in DStream
    
    # todo: Start the computation     
    
    # todo: Wait for the computation to terminate
    
    

