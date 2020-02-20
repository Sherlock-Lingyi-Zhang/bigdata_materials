# Spark Streaming - Lesson Plan

## Learning Objectives

In this section we will introduce spark streaming and its applications to continuous intelligence and ETL.

In this section, you'll learn

- Streaming applications and their typical architecture
- How to enable streaming in spark and connect to a streaming data source
- The concept of DStream and its operations
- Understand stateful multi-batch DStream operations and applications
- Understand streaming sources Kafka and Kinesis
- Understand fault tolerance in Spark Streaming
- Concept and applications of Structured Streaming

## Class 1: Intro to Spark Streaming

### Pre-work

**[slides](Spark8-SparkStreaming.pdf) / [print version](Spark8-SparkStreaming-Print.pdf)**

Watch the following clips on this topic, then complete the **self-assessment 21** below.

**Streaming Part1 Stream Processing (7:41)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/LOj7V113J4c" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming Part2 Streaming Architecture (5:55)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/-N0BLA1ASEY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming Part3 Sample Architecture (5:45)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/ICFbxeIuj1Y" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming Part4 Approaches of Stream Processing (6:16)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/hunYbXey3nk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming Part5 Create DStreams (9:54)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jkt5GEgQXGA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming Part6 DStream Operations (11:00)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/aB5WpenLuXQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming Part7 Streaming Word Count (7:02)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/CPgLUTe3Urc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming Part8 Twitter Example (8:50)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/AQLP3gbPfXk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 21** based on the materials in the above
- [Obtain twitter API credential needed for Spark Lab 10](sparklab10-twitterHashtag)

### In-Class

- Complete [Spark Lab 9: Streaming Word Count](sparklab09-StreamWordCount/README.md)
- Complete [Spark Lab 10: Live Dashboard for Twitter Hashtag](sparklab10-twitterHashtag)

## Class 2: 

**[slides](Spark9-SparkStreaming2.pdf) / [print version](Spark9-SparkStreaming2-Print.pdf)**

### Pre-work

Watch the following clips on this topic, then complete the **self-assessment 22** below.

**Streaming2 Part1 Stateful Operations (8:53)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/-1QgraJgw6Q" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming2 Part2 Windowed Operations (5:52)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/CVVgLyJ4p2A" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming2 Part3 Kafka Kinesis Integration (12:14)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/WoJ3J2fuzVI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming2 Part4 Fault tolerance (6:19)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/c5WK1vO2ptk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Streaming2 Part5 Structured Streaming (11:04)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/2ctUrRWinp0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 21** based on the materials in the above

### In-Class

- Complete [Spark Lab 11: Structured Streaming](sparklab11-StructuredStreaming/README.md)

## Additional Resources

### Books
- Chambers, Bill, and Matei Zaharia. "Spark: The Definitive Guide Big Data Processing Made Simple." (2018). [https://goo.gl/mitMRG](https://goo.gl/mitMRG) (Structured Streaming only)
- Mass and Garillot (2017) "Learning Spark Streaming". [https://goo.gl/9Jo2vK](https://goo.gl/9Jo2vK) (Spark Streaming)
- Learning Spark - Lightning Fast Data Analysis – by Karau, Konwinski, Wendell and Zaharia (O’Reilly) – Chapter 10, Spark Streaming (https://www.amazon.com/Learning-Spark-Lightning-Fast-Data-Analysis-ebook/dp/B00SW0TY8O). 

### Official Documentations
- [Spark Streaming programming guide](https://spark.apache.org/docs/latest/streaming-programming-guide.html) & links at the end of the page.
- [Structured Streaming Programming guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html), & links at the end of the page. 
- [Databricks Documentation on Structured Streaming](https://docs.databricks.com/spark/latest/structured-streaming/index.html) (with sample notebooks and connections to different streaming sources) 
- Official Spark Streaming API documentation: [Python](http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html), [Scala](https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.package).
- Official Structured Streaming API documentation: [Python](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.streaming), [Scala](https://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.streaming.package).
- [Getting Started with Spark Structured Streaming on Databricks](https://databricks.com/spark/getting-started-with-apache-spark/streaming#structured-streaming-overview)

### Talks and Videos

- [DataBricks Blocks on Structured Streaming](https://docs.databricks.com/spark/latest/structured-streaming/index.html)
    - Real-time Streaming ETL with Structured Streaming
    - Working with Complex Data Formats with Structured Streaming
    - Processing Data in Apache Kafka with Structured Streaming
    - Event-time Aggregation and Watermarking in Apache Spark’s Structured Streaming
    - Taking Apache Spark’s Structured Streaming to Production
    - Running Streaming Jobs Once a Day For 10x Cost Savings: Part 6 of Scalable Data
    - Arbitrary Stateful Processing in Apache Spark's Structured Streaming
- Databricks' Video Archives: [https://databricks.com/sparkaisummit/north-america/sessions](https://databricks.com/sparkaisummit/north-america/sessions) 
- [Introduction and Overview of Apache Kafka, TriHUG July 23, 2013](kafkatalk-trihug.pdf)
- [Deep Dive – Amazon Kinesis (Amsterdam Summit 2015)](amazonkinesis2015.pdf)
- [databricks - Spark Streaming by Tathagata Das (TD)  (2015?)](standford-td_streaming2015.pdf)
- [Spark and Spark Streaming @ Netflix (Spark Summit 2015)](NetflixStreaming2015.pdf)
- [A Deep Dive into Structured Streaming (Spark Summit 2016)](Structuredstreaming-sparksummit2016.pdf)
- [Spark Structured Streaming Helps Smart Manufacturing (by Intel Data Engineers, Spark Summit 2017)](EvenBriteSpark2019.pdf)
- [SPARK STREAMING PROGRAMMING TECHNIQUES YOU SHOULD KNOW (Spark Summit 2017)](StreamProgramTechniques2017.pdf)
- [Near Real-Time Analytics with Apache Spark (by Eventbrite Data Engineers, Spark AI Summit 2019)](EvenBriteSpark2019.pdf)
- [Data Warehousing with Spark Streaming @ Zalando (Spark AI Summit 2019)](sebastianherold2019.pdf)

### Sample Codes & Examples

- [Databricks Documentation on Structured Streaming](https://docs.databricks.com/spark/latest/structured-streaming/index.html) (with sample notebooks and connections to different streaming sources) 
- Python Streaming Examples (on Git): [https://github.com/apache/spark/tree/master/examples/src/main/python/streaming](https://github.com/apache/spark/tree/master/examples/src/main/python/streaming)
- [Spark Word Count pyspark Example](https://github.com/trustedanalytics/jupyter-default-notebooks/blob/master/notebooks/examples/spark/pyspark-streaming-wordcount.ipynb)
- [Big Data Processing with Apache Spark - Part 3: Spark Streaming](https://www.infoq.com/articles/apache-spark-streaming?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)
- [Streaming Architecture Examples](https://data-rider.blogspot.com/2015/07/spark-summit-2015-netflix.html)

