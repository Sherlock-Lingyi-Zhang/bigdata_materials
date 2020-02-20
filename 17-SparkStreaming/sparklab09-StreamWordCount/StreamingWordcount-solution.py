
# coding: utf-8

# # Streaming Wordcount

# In[ ]:

from pyspark.streaming import StreamingContext
ssc = StreamingContext(sc, 1)


# In[ ]:

# Create a DStream that will connect to localhost:9999
# Firewalls might block this!
lines = ssc.socketTextStream("localhost", 9999)


# In[ ]:

# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))


# In[ ]:

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)


# In[ ]:

# Print the first ten elements of each RDD generated in this DStream to the console
wordCounts.pprint()


# Now we open up a Unix terminal and type:
# 
#          $ nc -lk 9999
#      $ hello world any text you want
#      
# With this running run the line below, then type Ctrl+C to terminate it.

# In[ ]:

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate


# ### Utility: manually stop the spark streaming process 
# - this will also stop the spark kernel
# - alternatively you could do ssc.stop(false) to just stop the streaming process without terminate the spark kernel

# In[ ]:

ssc.stop()


# ### Utility: to stop the nc utility gracefully
# In case you cannot shut down the nc utility, the following would help you do so:
# - **pkill -f** allows you to kill a process by the command you used.

# In[ ]:

get_ipython().system(u"pkill -f 'nc -lk 9999'")

