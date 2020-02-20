# Introduction to Hadoop and Ecosystems

## Learning Objectives

The purpose of this module is to give you a quick overview of Hadoop and its ecosystem, which forms the core of the big data technology landscape. The ecosystem is quite complex and evolves quickly. We hope that through this introduction helps you to get a sense of where different pieces of technology fit into the bigger picture. We will also briefly introduce Sqoop.

In this section, you will learn

- The motivation behind Hadoop
- What Hadoop is and what significant features it provides
- How does it offer reliable storage for massive amounts of data with HDFS
- How does it support large scale data processing through MapReduce
- How Hadoop has evolved overtime
- What are key members of the Hadoop ecosystem
- The role of Hadoop in data centers
- How cloud computing has changed big data
- How to use sqoop to import RDBMS tables into Hadoop

## Class 1

### Pre Class

1. Please go through the [**Linux Command Line Essentials** module](../00-Linux/Linux-Practice.md), including lecture videos, practice problems, and **Self-assessment 1** (but not the Linux lab). 

2. Watch the following two clips on HDFS and MapReduce respectively, then complete the **self-assessment 2**: [Slides](Topic02-Hadoop.pdf) / [print](Topic02-Hadoop-print.pdf)

<iframe width="560" height="315" src="https://www.youtube.com/embed/V9pljlcp2ew" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/waBPMD5SJiY" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### During Class

- Intro to computing environment:  [slides](ComputingEnv.pdf) / [print](ComputingEnv-print.pdf)
- [Lab 0 - Essential Linux Commands](../00-Linux/lab0.md)
- Active quizzes on Intro to Hadoop
- Map Reduce Exercise

<!-- 2019-09-11 00:01:29: was not able to complete map Reduce exercise. move to the next one.  -->

## Class 2

### Pre Class 

1. Watch Introduction to Hadoop (3-4)

Watch the following two clips on Hadoop Ecosystem and trends respectively, then complete the **self-assessment 3**.

<iframe width="560" height="315" src="https://www.youtube.com/embed/okiR2M-a_tE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/8R-cKKGJQuE" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### During Class

<!-- 2019-09-11 00:01:29: was not able to complete map Reduce exercise. move to the next one.  -->
- Homework Requirements
- Go over homework 0 format. 
- MapReduce Exercises.
- Complete [lab 2: Running a Python MapReduce Job](lab02-mapreduce.md)

## Class 3 

### Pre Class

Watch a lecture video about Sqoop, then complete **Self-assessment 4**. [slides](Topic03-Sqoop.pdf) / [print](Topic03-Sqoop-Print.pdf)

<iframe width="560" height="315" src="https://www.youtube.com/embed/nXLgQtZqOiI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### During Class

- Lab Instructions: [slides](Topic02-Hadoop-Lab.pdf) / [print](Topic02-Hadoop-Lab-print.pdf)
- Complete [Lab 1: Using HDFS](lab01-hdfs.md). 
- Complete [lab 3: Using Sqoop to ingest relational data](lab03-scoop.md).  

## Assignments

- [**Homework Assignment 1**](homeworks/hw1/homework1.md): corresponds to this module and the next module (Linux, Hadoop MapReduce, Sqoop). 


## Resources

- [Lecture video for Hadoop Lab Instructions](https://www.youtube.com/embed/I0FERz9gmdw)

### Hadoop

- [Hadoop the definitive guide (book)](http://proquestcombo.safaribooksonline.com.ezp3.lib.umn.edu/book/databases/hadoop/9781491901687): A classic book on hadoop, but it requires some technical background (e.g. Java). **free access for U of M students**.
- [Hadoop File Systems Commands documentation](https://hadoop.apache.org/docs/r2.4.1/hadoop-project-dist/hadoop-common/FileSystemShell.html)
- [Hadoop HDFS Command Cheatsheet](http://images.linoxide.com/hadoop-hdfs-commands-cheatsheet.pdf): You can use `hadoop fs` to replace `hdfs dfs` (which are essentially the same for us [as explained here](https://stackoverflow.com/questions/18142960/whats-the-difference-between-hadoop-fs-shell-commands-and-hdfs-dfs-shell-co)) in the cheat sheet.
- [Ghemawat, Sanjay, Howard Gobioff, and Shun-Tak Leung. "The Google file system." ACM SIGOPS Operating Systems Review. Vol. 37. No. 5. ACM, 2003. ](Ghemawat2003.pdf): Original Google file system paper
- [Dean, Jeffrey, and Sanjay Ghemawat. "MapReduce: simplified data processing on large clusters." Communications of the ACM 51.1 (2004): 107-113.](dean2004.pdf): Original MapReduce paper
- [Shared nothing architectures](https://www.oreilly.com/learning/processing-data-in-hadoop): an excerpt from Hadoop Application Architectures, by Mark Grover, Ted Malaska, Jonathan Seidman, and Gwen Shapira. This article explains how Sharing Nothing gives Hadoop's data processing frameworks scalability and fault tolerance. It also has an in-depth overview of Hadoop MapReduce.
- [Introduction to Data Lakes](IntroToDataLakes.pdf): Chapter 1 of the book by Alex Gorelik titled "[The Enterprise Big Data Lake (2019)](http://shop.oreilly.com/product/0636920042204.do)"

### Hadoop Versions Evolvement

- [Difference between Hadoop 1 and Hadoop 2](https://www.journaldev.com/8806/differences-between-hadoop1-and-hadoop2) (Links to an external site.)Links to an external site.
- [Introduction to Hadoop 2 and its advantages (2019)](
https://www.edureka.co/blog/introduction-to-hadoop-2-0-and-advantages-of-hadoop-2-0/) 
- [Apache Hadoop 2: migration from 1.0 to 2.0 (2014)](https://www.slideshare.net/tshooter/strata-conf2014)
- [Apache Hadoop 2: migration from 1.0 to 2.0 - 2014](https://www.slideshare.net/tshooter/strata-conf2014)
- [Hortonworks: How Apache Hadoop 3 Adds Value Over Apache Hadoop 2 (2018)](https://hortonworks.com/blog/hadoop-3-adds-value-hadoop-2/)

### sqoop

- [Sqoop user guide](http://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html): Your "go-to" page for scoop usage details. 

- [Apache Sqoop Cookbook (2013 book by O’Reily) ](http://shop.oreilly.com/product/0636920029519.do): This handy cookbook provides dozens of ready-to-use recipes for using Apache Sqoop, the command-line interface application that optimizes data transfers between relational databases and Hadoop.

- [Official Documentation for Sqoop 2](https://sqoop.apache.org/docs/1.99.7/index.html): Note- Sqoop 2 is still in development, not yet for production use.
