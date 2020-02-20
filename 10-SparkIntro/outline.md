# Introduction to Spark

## Learning Objectives

Spark has quickly surpassed Hadoop to become a multi-purpose parallel computing framework for big data. 

In this section, you will learn:

- What is Spark?
- Why Apache Spark?
- Spark Programming Model
- Spark Architecture and Integration with Hadoop
- Spark Use Cases

---

- How do spark programs work?
- How RDDs are created from files or data in memory
- Commonly used RDD transformations
- Commonly used RDD actions
- Understand a typical life-cycle of a Spark program.

## Class 1

In this class, we introduce Apache Spark and the core concepts of Spark RDD (including how to create it). For this module, you may check out the Book "Learning Spark" from the resources section.

### Pre-work

1\. **Lecture Video: Intro to Spark**

**[slides](Spark1-Intro.pdf) / [print version](Spark1-Intro-Print.pdf)**

Clip 1 - What is Spark and Why Spark (17:08)

<iframe width="560" height="315" src="https://www.youtube.com/embed/V7468COkfrk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Clip 2 - Spark RDD, Architecture, and Use Cases (16:25)

<iframe width="560" height="315" src="https://www.youtube.com/embed/4ZLhoLSOvGg" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

2\. Complete **self-assessment 12** on Canvas.

3\. Jupyter Notebook tutorial (Optional)

Complete [Spark Lab 0: Jupyter Notebook tutorial](sparklab00/README.md): A quick Jupiter notebook tutorial (if you're already familiar with it, you can skip this).

4\. Watch the following clips on the introduction to Spark RDDs, then complete the **self-assessment 12**.

**[slides](Spark2-RDDs.pdf) / [print version](Spark2-RDDs-print.pdf)**

Clip 1 - Spark Programming Environment (10:54)

<iframe width="560" height="315" src="https://www.youtube.com/embed/E08JTWZQulo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Clip 2 - RDDs and Parallelize (9:46)

<iframe width="560" height="315" src="https://www.youtube.com/embed/zwW9VI_7feA" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Clip 3 - Create RDD from file source (6:43)

<iframe width="560" height="315" src="https://www.youtube.com/embed/LFRkN3w_ZzU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

5\. Complete **self-assessment 13** on Canvas.

6\. Set up Using Spark Environments

- [Configure and use Spark Environments](../faqs/sparkenv.md): List different Spark environment available to you and their pros and cons.

7\. If you need additional reading to help you understand Spark (and RDD), 

The book "Learning Spark", By Holden Karau, Andy Konwinski, Patrick Wendell, Matei Zaharia (at the end of the resources) may be helpful. 

### In Class

- Complete [Spark Lab 1: Explore RDDs Using the Spark Shell](sparklab01/README.md) 
   + [PySpark solution](sparklab01/sparklab01-solution.md)
   + [Scala solution](sparklab01/sparklab01-solution-scala.md)

In this lab you will start the Spark Shell and read a text file into a Resilient Distributed Data Set (RDD). 

- Complete [Spark Lab 1x: Create RDDs](sparklab01x-CreateRdd/README.md)
   + [PySpark solution (view only)](sparklab01x-CreateRdd/sparklab01x-solution.html)

- Discuss
    - Why spark is faster than mapreduce
    - Spark programming framework
    - Spark use cases

## Class 2

In this class, we continue to introduce RDDs, including the key transformation and action APIs. 

### Pre-work

**[slides](Spark2-RDDs.pdf) / [print version](Spark2-RDDs-print.pdf)**

Clip 4 - RDD Transformations (11:38)

<iframe width="560" height="315" src="https://www.youtube.com/embed/SVw1gbinUBc" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Clip 5 - RDD Actions (7:41)

<iframe width="560" height="315" src="https://www.youtube.com/embed/XnNStkSA-X0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Clip 6 - RDD cache and Demo (9:06)

<iframe width="560" height="315" src="https://www.youtube.com/embed/xMT3vzpdcFU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **Self-assessment 14** on Canvas

- Check out the **"Transformations and Actions - A visual Guide of the API"** in the resources section for more help in visually understanding transformation and action APIs. 

### In-Class

- discuss: nature of lazy execution
- Complete [Spark Lab 2: Use RDDs to Transform a Dataset](sparklab02-RDD-transform/README.md)
    + [PySpark solution](sparklab02-RDD-transform/sparklab2-solution.html)
    + [Scala solution](sparklab02-RDD-transform/sparklab2-scala-solution.md)
- Complete [Spark Lab 3: Process Data Files with Spark RDD](sparklab03-RDD-ProcessFiles/README.md)
    + [PySpark solution](sparklab03-RDD-ProcessFiles/sparklab3-solution.html)
    + [Scala solution](sparklab03-RDD-ProcessFiles/sparklab3-scala-solution.html)

## Assignments

- [**Homework Assignment 4: Spark RDD**](../homeworks/hw4/README.md)

## Resources and Additional Readings

### Spark Use cases

- [MetronicUseCase.pdf](MetronicUseCase.pdf)
- [toyota-spark-use-cases.pdf](toyota-spark-use-cases.pdf)
- [Whitmore_Brian-VerticaUseCase.pdf](Whitmore_Brian-VerticaUseCase.pdf)
- [TopApacheSparkUseCases_Qubole.pdf](TopApacheSparkUseCases_Qubole.pdf)

### Spark

- [(book) Learning Spark, By Holden Karau, Andy Konwinski, Patrick Wendell, Matei Zaharia](https://primo.lib.umn.edu/primo-explore/fulldisplay?docid=UMN_ALMA51641437080001701&context=L&vid=TWINCITIES&lang=en_US&search_scope=mncat_discovery&adaptor=Local%20Search%20Engine&isFrbr=true&tab=article_discovery&query=any,contains,Learning%20Spark): **free access for U of M students**. This book is relatively old (2015). It has good information on Core spark (RDD). The information on Spark SQL/Spark Streaming/MLlib is out of date, but still provides some value.
- [Beginning Apache Spark 2 : with resilient distributed datasets, Spark SQL, structured streaming and Spark Machine Learning library. By Hien Luu, 2018](https://primo.lib.umn.edu/primo-explore/fulldisplay?docid=UMN_ALMA51725726230001701&context=L&vid=TWINCITIES&lang=en_US&search_scope=mncat_discovery&adaptor=Local%20Search%20Engine&tab=article_discovery&query=any,contains,learning%20spark).  This book is more current (but does not seem to be thorough). You may use it as a handbook to read more about different modules of Apache Spark. The examples given are all in Scala though. [Local pdf copy](2018_Book_BeginningApacheSpark2.pdf).
- [Official Spark Programming Guides](https://spark.apache.org/docs/latest/index.html): good/authoritative source of information; introductory. If you need references, you need to go to API docs.
- [Spark Python API Docs](https://spark.apache.org/docs/latest/api/python/index.html): Official references for spark Python API
 
- [Transformations and Actions - A visual Guide of the API](https://training.databricks.com/visualapi.pdf): see a rather good (and visual source of information about RDD transformations and actions)
- [Databricks training resources and links therein](http://databricks.com/spark-training-resources): a lot of these are old though.
- [Spark vs. Hadoop MapReduce by Saggi Neumann](https://www.xplenty.com/blog/2014/11/apache-spark-vs-hadoop-mapreduce)
- [Spark: Making Big Data Interactive and Real-Time](https://www.sics.se/sites/default/files/pub/mateizahariasics-cloud-day-2.pdf)
- [Big Data Processing with Apache Spark - Part 3: Spark Streaming](https://www.infoq.com/articles/apache-spark-streaming?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)
- [Big Data Processing with Apache Spark - Part 4: Spark Machine Learning](https://www.infoq.com/articles/apache-spark-machine-learning)

## Scala

- [Scalatutorials.com (their executor is broken, but their examples are pretty good)](http://scalatutorials.com)
- [Scala Tutorial](https://www.youtube.com/watch?v=DzFt0YkZo8M): Youtube video 1 hour
- [Scala Tutorial](https://www.tutorialspoint.com/scala/index.htm): more systematic tutorial on Scala
- [Scala cheatsheet ](http://docs.scala-lang.org/cheatsheets): with common mistakes
