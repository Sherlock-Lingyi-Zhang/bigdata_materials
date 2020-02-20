# Introduction to Hive

## Learning Objectives

The purpose of this module is to give you a quick overview of Hive and HiveQL syntax and features, so that you can already use your SQL knowledge to conduct data analysis using Hive. In the subsequent modules, we will dive deeper into Hive's data modeling and optimization aspects. 

In this section, you will learn:

- What Hive is
- How Hive differs from a relational database
- Ways in which organizations use Hive
- How to invoke and interact with Hive
- How to explore databases and tables in Hive
- How HiveQL syntax compares to SQL
- Which data types Hive supports
- Which types of join operations Hive supports and how to use them

This module is split into two parts, Introduction to Hive and Relational Data Analysis with Hive (HiveQL). Each part comes with an assessment. The first part cover the first four bullets in the above. 

---

## Pre-work

Watch the following clips, then complete the **self-assessments 5 and 6**.

### Intro to Hive

**[slides](Hive1-Intro.pdf) / [print version](Hive1-Intro-print.pdf)**

**what is Hive, why Hive, Hive vs RDBMS  (17:43)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/E7LzEYRsxFc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Hive Use Cases, Interact with Hive, Conclusion (10:28)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/SZxQRQ2VX2M" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Based on the above, complete **self-assessment 5** on Canvas.

### HiveQL

**[slides](Hive2-DataAnalysis.pdf) / [print version](Hive2-DataAnalysis-Print.pdf)**

In the next part, we discuss the feature and limitations of HiveQL, especially compared with the SQL dialect such as MySQL. We assume that you have already have SQL knowledge so that we can focus on the differences. 

**HiveQL Syntax, Text Functions, and Subqueries (13:23)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/vjxJw5Kb6u4" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Hive Data Types and Joins (5:47)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/hWbADTEsA20" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 6** on Canvas.

### During Class

- Discuss: Hive Managed Table and External Table
- Discuss: Hive vs Relational Databases

- Complete [Lab 6: Running Hive Queries from the Shell, Scripts, and Hue ](lab06-intro.md): the purpose of this lab is to learn to how to interact with Hive in a few different ways.
    - [solution](lab06-intro-solution.md)
- Complete [Lab 7: Using HiveQL to Analyze an Advertising Campaign](lab07-hiveql.md): this lab gives you a good dose of practice on using joins, subqueries, and functions in Hive. 
    - [solution](lab07-hiveql-solution.md)
- Complete [Lab 7x: Using Complex Fields in Hive](lab07x-complexfields.md): this lab gives you a good dose of practice on using joins, subqueries, and functions in Hive. 
    - [solution](lab07x-complexfields-solution.md)

---

## Resources

### Hive Features and Evolvement
- [Cloudera Apache Hive Page](https://www.cloudera.com/products/open-source/apache-hadoop/apache-hive.html)
- [Introduction to Hive 2 and LLAP](https://hortonworks.com/blog/announcing-apache-hive-2-1-25x-faster-queries-much/)
- [Horton's Introduction to Hive 3](https://www.slideshare.net/thejasmn/hive-3-a-new-horizon-121226317)
- [LLAP: Live Long And Process](https://cwiki.apache.org/confluence/display/Hive/LLAP)
- [Migrating from Hive CLI to Beeline: A Primer](http://blog.cloudera.com/blog/2014/02/migrating-from-hive-cli-to-beeline-a-primer/)
- [Tez vs MapReduce @ Hortonworks](https://community.hortonworks.com/questions/83394/difference-between-mr-and-tez.html)

### HiveQL Featurs, Examples, and Tutorial
- [Programming Hive (book)](http://proquestcombo.safaribooksonline.com.ezp3.lib.umn.edu/book/databases/hadoop/9781449326944): **free access for U of M students**
- [Hive command with examples](https://www.edureka.co/blog/hive-commands-with-examples)
- [Hive Function Examples](http://hadooptutorial.info/hive-functions-examples/)
- [Hive Windowing and Analytics Functions](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+WindowingAndAnalytics)
- [Hive Build in Functions](https://cwiki.apache.org/confluence/display/Hive/Tutorial)
- [A full list of Hive Functions](http://svn.apache.org/viewvc/hive/trunk/ql/src/java/org/apache/hadoop/hive/ql/exec/FunctionRegistry.java?view=markup)
- [Hive Join & SubQuery Tutorial with Examples](https://www.guru99.com/hive-join-subquery.html#8)

### Hive use cases
- [Data Analysis with Hadoop and Hive at Orbitz](http://www.slideshare.net/jseidman/data-analysis-with-hadoop-and-hive-chicagodb-2212011): slides
- [Sentiment Analysis Using Apache Hive (example)](http://blog.xebia.com/sentiment-analysis-using-apache-hive/)
- [Hadoop Analysis of Apache Logs Using Flume-NG, Hive and Pig](http://cuddletech.com/?p=795) 
- [How To Refine and Visualize Server Log Data with Hadoop: HortonWorks Sandbox Tutorial, Flume + Hive](https://hortonworks.com/blog/hadoop_tutorial_visualizing_server_logs/)
- [Twitter, Flume, Hive](http://www.irdindia.in/journal_ijraet/pdf/vol4_iss2/27.pdf)
- [integrating flink with hive (Alibaba Talk 2019)](https://www.slideshare.net/BowenLi9/integrating-flink-with-hive-xuefu-zhang-and-bowen-li-seattle-flink-meetup-feb-2019): slides