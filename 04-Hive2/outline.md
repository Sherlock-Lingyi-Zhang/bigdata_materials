# Hive Data Modeling and Optimization

## Learning Objectives

The purpose of this module is to discuss the decisions you must make in creating Hive tables and how to populate these tables with data and how to take data out. A related topic is how you can optimize Hive query performance by making better choices in table formats, underlying execution engines, table partitioning and writing better queries. 

In this section, you will learn:

- How Hive encodes and stores data by default
- How to create Hive databases and tables
- How to load data into tables
- How to alter and remove tables
- How to save query results into tables and files
- How to use faster engines for Hive
- How to choose storage formats for Hive tables
- How to partition tables to reduce amount of data read for a query
- How to understand and write better performing Hive queries


This module is split into two parts, Hive Data Modeling and Hive Optimization. Each part comes with an assessment and a lab. The first part cover the first five bullets in the above. 

---

## Class 1\. Hive Data Modeling

### Pre-work

**[slides](Hive3-DataModel.pdf) / [print version](Hive3-DataModel-Print.pdf)**

Watch the following clips on this topic, then complete the **self-assessment 7**.

**Create and Load Hive Tables (13:23)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZjNe0SNgE8Q" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


**Drop Tables and Export Results (5:46)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/5fxYfloq0qE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 7** on Canvas.


### During Class

- Complete [Lab 8: Data Management with Hive ](lab08-datamodel.md): the purpose of this lab is to learn to common techniques for creating and populating Hive tables.
    - [solution](lab08-datamodel-solution.md)
- Complete [Lab 8x: Using CSV Serde](lab08x-csvserde.md): 
    - [solution](lab08x-csvserde-solution.md)

---

## Class 2\. Hive Optimization

### Pre-work

**[slides](Hive4-HiveOpt.pdf) / [print version](Hive4-HiveOpt-Print.pdf)**

Slow Hive performance is a common issue and results in low productivity and wasteful resource utilization. In this lesson, we discuss several ways that can make your Hive query run faster. 

After the lecture, please then complete the **self-assessment 8**.

**Intro & Choose Execution Engine (3:36)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/MfiPgzbTsrY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Choose Hive Storage Options (13:27)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/dAAy9yHk9Lc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 8** on Canvas.

### During Class 

- Complete [Lab 9: Hive Optimization](lab09-hiveopt.md): this lab gives you a good dose of practice on using joins, subqueries, and functions in Hive.
    - [Solution](lab09-hiveopt-solution.md)
    
## Class 3\. Hive Optimization (Cont.)

### Pre-work

**[slides](Hive4-HiveOpt.pdf) / [print version](Hive4-HiveOpt-Print.pdf)**

After watching the following lecture videos, please then complete the **self-assessment 9**.

**Partition Table (16:05)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/11mvOdUOWoY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


**Sort By and Bucketing (13:23)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/StennIkhlPk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 9** on Canvas.

### During Class 

- Complete [Lab 9: Hive Optimization](lab09-hiveopt.md): this lab gives you a good dose of practice on using joins, subqueries, and functions in Hive.
    - [Solution](lab09-hiveopt-solution.md)

---

## Assignments

- **Homework Assignment 2** corresponds to this and the previous Hive modules.

---

## Resources

### Data Modeling

- [Hive LanguageManual Data Definition Language](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL)
- [Using Sqoop to Move Data into Hive](https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.6.5/bk_data-access/content/using_sqoop_to_move_data_into_hive.html)

### Hive Optimization

- [Hive Performance – 10 Best Practices for Apache Hive](https://www.qubole.com/blog/hive-best-practices/)
- [Hive Optimization Techniques With Examples](https://acadgild.com/blog/hive-optimization-techniques-with-examples)
- [Optimize Apache Hive queries in Azure HDInsight](https://docs.microsoft.com/en-us/azure/hdinsight/hdinsight-hadoop-optimize-hive-query)
- [Performance comparison of different file formats and storage engines in the Apache Hadoop ecosystem (2017)](https://db-blog.web.cern.ch/blog/zbigniew-baranowski/2017-01-performance-comparison-different-file-formats-and-storage-engines)
- [Hive Parquet](https://cwiki.apache.org/confluence/display/Hive/Parquet)
- [Dremel made simple with Parquet (2013)](https://blog.twitter.com/engineering/en_us/a/2013/dremel-made-simple-with-parquet.html)
- [Google's Dremel paper (on which Parquet is based) (2010)](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/36632.pdf)
- [ORC file format](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+ORC)
- [ORCFile in HDP 2: Better Compression, Better Performance (2013)](https://hortonworks.com/blog/orcfile-in-hdp-2-better-compression-better-performance/)
- [Hive Lanaguage manual - Sort By](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+SortBy)
- [Hive Lanaguage manual - Explain](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+Explain)
- [Hive Lanaguage manual - Bucketing](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL+BucketedTables)
- [Hive Lanaguage manual - Partition](https://cwiki.apache.org/confluence/display/Hive/Tutorial#Tutorial-Dynamic-PartitionInsert)