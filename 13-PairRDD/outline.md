# Working with Pair RDDs

## Learning Objectives

In this section we will introduce a special kind of RDD called pair RDDS, that are particularly useful for map-reduce style parallel computation in Spark. These will come handy, for example for joining data, aggregating data, sorting etc.

In this section, you’ll learn
- What is a Pair RDD?
- How to create Pair RDDs
- Special operations available on Pair RDDs
- How map­‐reduce algorithms are implemented in Spark

## Pre-work

**[slides](Spark4-PairRDDs.pdf) / [print version](Spark4-PairRDDs-Print.pdf)**

Watch the following clips on the key-value pair RDDs, then complete the **self-assessment 15**.

Clip 1 - Create Pair RDDs (10:29)

<iframe width="560" height="315" src="https://www.youtube.com/embed/eOKeIUE5S1w" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Clip 2 - Pair RDD operations (20:28)

<iframe width="560" height="315" src="https://www.youtube.com/embed/6CzJfrz3yJk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Clip 3 - Pair RDDs and MapReduce (5:26)

<iframe width="560" height="315" src="https://www.youtube.com/embed/jArlIctlb7w" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **Self-assessment 15**.

- If you need additional reading, please check out relevant sections of online books in the resources section.

## In-Class

- Complete [Spark Lab 4: Use Pair RDDs to join two datasets](sparklab04-PairRDD-Join/README.md)

## Assignments

- [**Homework Assignment 4: Spark RDD**](../homeworks/hw4/README.md)

 
## Additional Resources

- [(book) Learning Spark, By Holden Karau, Andy Konwinski, Patrick Wendell, Matei Zaharia](https://primo.lib.umn.edu/primo-explore/fulldisplay?docid=UMN_ALMA51641437080001701&context=L&vid=TWINCITIES&lang=en_US&search_scope=mncat_discovery&adaptor=Local%20Search%20Engine&isFrbr=true&tab=article_discovery&query=any,contains,Learning%20Spark): **free access for U of M students**. This book is relatively old (2015). It has good information on Core spark (RDD). The information on Spark SQL/Spark Streaming/MLlib is out of date, but still provides some value.
- [Beginning Apache Spark 2 : with resilient distributed datasets, Spark SQL, structured streaming and Spark Machine Learning library. By Hien Luu, 2018](https://primo.lib.umn.edu/primo-explore/fulldisplay?docid=UMN_ALMA51725726230001701&context=L&vid=TWINCITIES&lang=en_US&search_scope=mncat_discovery&adaptor=Local%20Search%20Engine&tab=article_discovery&query=any,contains,learning%20spark) Click the SpringerLink Books link. **free access for U of M students**. Obviously this book is more current (but does not seem to be thorough). You may use it as a hand book to read more about different modules of Apache Spark. The examples given are all in Scala though.  [Local pdf copy](../10-SparkIntro/2018_Book_BeginningApacheSpark2.pdf).
- [Pair RDD Class documentation](https://spark.apache.org/docs/latest/api/java/org/apache/spark/rdd/PairRDDFunctions.html): to get a comprehensive class of pair RDD operations and a brief description. 
- [Avoid GroupByKey (databrick)](https://databricks.gitbooks.io/databricks-spark-knowledge-base/content/best_practices/prefer_reducebykey_over_groupbykey.html): A good explanation of why avoiding groupByKey. 