# Data Frames and Spark SQL

## Learning Objectives

Spark DataFrame is Spark's module  for structured data processing. It provides powerful APIs for SQL style processing and ETL capabilities for other modules including MLlib and spark streaming. 

In this section, you will learn:

- In this module you will learn
- What Spark SQL is
- How to create a DataFrame
- How to query data in a DataFrame
- How to manipulate data with DataFrame
- Comparison between Spark SQL, Hive, and Impala

**[slides](Spark5-SparkSQL.pdf) / [print version](Spark5-SparkSQL-Print.pdf)**

## Class 1

### Pre-work

Watch the following clips on this topic, then complete the **self-assessment 16**.

As you watch the lecture videos, **You may open a blank notebook and go along using the demo data** (downloadable in a zip file here [http://idsdl.csom.umn.edu/c/share/msba6330/sparksql_demos.zip](http://idsdl.csom.umn.edu/c/share/msba6330/sparksql_demos.zip)). 

In the data.zip, we have:

- iris.json (data file)
- pcodes.csv (data file)
- people.csv (data file)
- people.json (data file)
- peopleheader.csv (data file)
- people-no-pcode.csv (data file)
- Aggregation Demo.ipynb  (completed demo notebook)
- CreateDataFrameDemo.ipynb (completed demo notebook)
- DataFrameManipulationsDemo.ipynb (completed demo notebook)
- DataFrameOperationsDemo.ipynb (completed demo notebook)
- joinViewRddDemo.ipynb (completed demo notebook)

The completed notebooks for demos are not perfectly aligned with what's shown in the lecture video. 

---

### Lecture Videos Part I.

**SparkSQL Part 1 Intro to Spark DataFrame & Spark SQL (6:21)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/KyjwjU5E-mc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 2 Create DataFrame from RDDs (8:26)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/oY49UvHhN3c" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 3 Create DataFrame from File/DB Sources (10:44)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/IeZZv6qRcVA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 4 Save DataFrames (4:22)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/NmLsNlkg6hc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 5 DataFrame Actions and Meta Operations (8:53)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/COqe6hOj3iw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 6 DataFrame Queries (18:39)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/lFSvza-GHa0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 16** based on the materials in the above

### In-Class

- Differences between DataFrame and RDD
- Complete [Spark Lab 5:Using Spark SQL ](sparklab05-SQL/README.md)

## Class 2

### Pre-Work 

Watch the following clips on this topic, then complete the **self-assessment 17**. As you watch, you may open a blank notebook and follow along using the demo data downloaded in the previous class.

**SparkSQL Part 7 Data Manipulation Queries (8:28)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/1USVOrR7dAs" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 8 Select, Filter, Sort (8:57)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/VML1UYPtQX0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 9 Aggregation and Windowing (19:30)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/micjBNE7kUU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 10 Join, Tables, and Views (16:20)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/sXy52wrwOiY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**SparkSQL Part 11 Relationship with RDD, Impala, Hive (9:57)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/V9nekY-5QJM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 17** based on the materials in the above

### In-Class

- Complete [Spark Lab 6:Use Spark SQL to Join and Aggregate Data ](sparklab06-SQL-JoinAgg/README.md) 


## Assignments

- [**Homework Assignment 5: Spark SQL**](../homeworks/hw5/README.md)

## Resources

- [Office Documentation from Spark](http://spark.apache.org/docs/latest/sql-programming-guide.html#sql)
- [Spark SQL Dataframe API (Python) ](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html)
- [Spark SQL Dataframe API (Scala)](http://spark.apache.org/docs/latest/api/scala/index.html#org.apache.spark.sql.Dataset)
- [Spark & Python: SQL & DataFrames - Codementor tutorial ](https://www.codementor.io/spark/tutorial/python-spark-sql-dataframes)
- [Complete Guide on DataFrame Operations in PySpark](https://www.analyticsvidhya.com/blog/2016/10/spark-dataframe-and-operations/)
- [FROM PANDAS TO APACHE SPARK’S DATAFRAME](https://ogirardot.wordpress.com/2015/07/31/from-pandas-to-apache-sparks-dataframe/?source=post_page---------------------------)
- [Introducing Window Functions in Spark SQL](https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html)

