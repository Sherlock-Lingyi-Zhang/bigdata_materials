# NoSQL - Lesson Plan

## Learning Objectives

In this section we will introduce NoSQL data stores and their use cases.

In the first class, you'll learn

- Understand strengths and limitations of traditional SQL databases
- Understand common characteristics of NoSQL databases
- Understand the trade-offs facing distributed databases in light of the CAP theorem
- Distinguish between ACID and BASE consistency models
- Be familiar with different types of NoSQL / NewSQL databases and their use cases
- Understand the complexity of choosing different database technologies for big data applications

In the second class, we will focus on one of the leading NoSQL products, Amazon's DynamoDB. In this class, you will learn:

- Understand the characteristics and use cases of DynamoDB
- Understand DynamoDB's data model
- Understand the different ways to interact with DynamoDB
- Be familiar with the design patterns for DynamoDB
- Understand the ecosystem around DynamoDB

## Class 1: Intro to NoSQL

### Pre-work

**[slides](NoSQL.pdf) / [print version](NoSQL-Print.pdf)**

Watch the following clips on this topic, then complete the **self-assessment 23** below.

**Part1 RDBMS has a scale problem (7:02)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/s4YaYJr26vw" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part2 What Is NoSQL (8:13)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/Gw-hEeGr8m8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part3 CAP Theorem (8:44)** 

<iframe width="560" height="315" src="https://www.youtube.com/embed/hY6n8BdbUHo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part4 Key Value and Wide Column Stores (11:30)** 

<iframe width="560" height="315" src="https://www.youtube.com/embed/lJLfmVnmxrI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part5 Document and Graph Databases, NewSQL (9:37)** 

<iframe width="560" height="315" src="https://www.youtube.com/embed/NSRkZabKwRo" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part6 How to Choose (8:12)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/kbBBBymHQGk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 23** based on the materials in the above

### In-Class

- Discussion questions no NoSQL
- Go over slides:  **[slides](graphFrame.pdf) / [print version](graphFrame-Print.pdf)**
- Complete [Lab 14: Graph Analytics using Spark GraphFrames](lab14-graphframes/README.md)


## Class 2: DynamoDB: Amazon's Highly Available Key-value Store

### Pre-work

**[slides](DynamoDB.pdf) / [print version](DynamoDB-Print.pdf)**

Watch the following clips on this topic, then complete the **self-assessment 24** below.

If you have time, we also recommend you to read the original papers on BigTable and DynamoDB listed below in the resources section.

**Part1 Introduction (8:09)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/aYx5MYE56M8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part2 Data model and Primary Keys (12:45)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/oHCEZWqAwfk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part3 Indexes (13:25)** 

<iframe width="560" height="315" src="https://www.youtube.com/embed/zrubLzvU_tI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part4 Operations and Interfaces (5:31)** 

<iframe width="560" height="315" src="https://www.youtube.com/embed/OinbMsr267c" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

**Part5 Modeling Patterns and Architecture (15:46)** 

<iframe width="560" height="315" src="https://www.youtube.com/embed/dG_fXmuEi4g" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

- Complete **self-assessment 24** based on the materials in the above

### In-Class

Complete [Lab 15: Amazon DynamoDB](lab15-dynamodb/README.md)

## Additional Resources

### NoSQL

#### Talks and Videos

- [Scalable Data Management: An In-Depth Tutorial on NoSQL Data Stores](nosql-tutorialbtw2017.pdf): A 326 page tutorial on NoSQL given by Felix Gessert, Wolfram Wingerath, Norbert Ritter in 2017 Workshp on business Technology and Web (a main source of reference for our slides).
- [Choosing the Right NoSQL Database @ edureka!, 2014](https://www.edureka.co/blog/choosing-the-right-nosql-database/): A recorded video/slides the webinar on the topic “Choosing the Right NoSQL Database – MongoDB® Vs Cassandra Vs HBase, which was conducted on 7th June 2014.

#### Publications & Blog Articles

- [Bigtable: A Distributed Storage System for Structured Data](bigtable-osdi06.pdf):the original BigTable paper by Google in OSDI 2006.
- [Dynamo: Amazon’s Highly Available Key-value Store, 2007](amazon-dynamo-sosp2007.pdf): the original Dynamo paper by Amazon in SOSP 2007.
- [[book]A Deep Dive into NoSQL Databases: The Use Cases and Applications, 2018](https://www.sciencedirect.com/bookseries/advances-in-computers/vol/109/suppl/C): A recent book on NoSQL (**free e-book pdfs** for U of M students).  It has some indepth coverage of NewSQL in-memory databases. Its chapter six also has hands-on examples of various kinds of NoSQL databases.
- [A Real Comparison Of NoSQL Databases HBase, Cassandra & MongoDB, 2015 by Birendra Kuma Sahu](https://www.linkedin.com/pulse/real-comparison-nosql-databases-hbase-cassandra-mongodb-sahu/): A short read on comparisons across different popular nosql databases.
- [10 use cases where NoSQL will outperform SQL, network World 2015](https://www.networkworld.com/article/2999856/10-use-cases-where-nosql-will-outperform-sql.html): a quick read on kinds of nosql applications.
- [7 Steps to Understanding NoSQL Database, KDNuggets article by Matthew Mayo](https://www.kdnuggets.com/2016/07/seven-steps-understanding-nosql-databases.html)

#### Sample Codes & Examples

- [Datacamp MongoDB course](https://www.datacamp.com/courses/introduction-to-using-mongodb-for-data-science-with-python):
Introduction to MongoDB in Python on DataCamp.

### Spark GraphFrames 

#### Official Documentations
- [Spark GraphFrames Python API documentation](https://graphframes.github.io/graphframes/docs/_site/api/python/index.html)
- [Graph Frames Official Github Page & Overview](https://graphframes.github.io/graphframes/docs/_site/index.html)
- [Databricks graphframes tutorial](https://docs.databricks.com/spark/latest/graph-analysis/graphframes/graph-analysis-tutorial.html)
- [GraphFrames User Guide by Databricks](https://docs.databricks.com/spark/latest/graph-analysis/graphframes/user-guide-python.html)

#### Talks and Presentations
- [GraphFrames: Graph Queries in Spark SQL](https://www.youtube.com/watch?v=zx9KI3DsZss): (Berkeley) Ankur Dave's 2016 Spark Submit talk introducing GraphFrames. [the slide deck](GraphFrames2016.pdf)
- [A Tale of Two Graph Frameworks on Spark: GraphFrames and Tinkerpop - Artem Aliev & Russell Spitzer](https://www.youtube.com/watch?v=DW09q18OHfc): Spark Submit 2017 talk on Spark GraphX vs Spark GraphFrame.

#### Examples
- [a more complex example of graphframes using flight data, by Databricks](https://databricks.com/blog/2016/03/16/on-time-flight-performance-with-graphframes-for-apache-spark.html)
- [An introduction to Spark GraphFrame with examples analyzing the Wikipedia link graph](https://towardsdatascience.com/an-introduction-to-spark-graphframe-with-examples-analyzing-the-wikipedia-link-graph-67e58c20a107)

### DynamoDB

#### Talks and Videos

- [Amazon DynamoDB by Nicolas Travers, 2016](travers2016_Dynamo.pdf): this slide deck contains some inside look at DynamoDB's architecture, including how it implements partition, data versioning, etc.
- [From SQL to NoSQL: Best Practices for Migrating from RDBMS to DynamoDB, 2016](sqltonosql-bestpractices.pdf) by Rick Houlihan, Amazon's Principal Solutions Architect, focusing on from sql to nosql mitgration.
- [Introduction to DynamoDB, 2016](intro2dynamodb.pdf) by Rick Houlihan, Amazon's Principal Solutions Architect, our main reference. [Youtube link](https://www.youtube.com/watch?v=jL-WJlBtpIw&feature=youtu.be).
- [Best Practices for Migrating from RDBMS to Amazon DynamoDB, 2015](migration-rdbms-to-dynamodb.pdf): how to migrate from RDBMS to DynamoDB by AWS 2015. 
- [Dynamo: Amazon’s Highly Available Key-value Store & Amazon DynamoDB, 2013](dynamo_dynamodb.pdf) by Zuhair Khayyat; one of Amazon's early report at Dynamo and DyanmoDB. 
- [AWS re:Invent 2014: From Zero to NoSQL Hero - Amazon DynamoDB Tutorial (BDT203)](https://www.youtube.com/watch?v=tDqLwzQEOmM&feature=youtu.be): Youtube video on Amazon's DynamoDB tutorial. 

#### Publications
- [Comparing the Use of Amazon DynamoDB and Apache HBase for NoSQL 2018](AWS_Comparing_DynamoDB_HBase.pdf): Amazon's white paper on comparing dynamodb and HBase.
- [DynamoDB by tutorialspoint, 2016](dynamodb_tutorial.pdf): Tutorialpoint's coverage on dynamoDB; more like a handbook and users manual.
- [Dynamo: Amazon’s Highly Available Key-value Store, 2007](amazon-dynamo-sosp2007.pdf): the original paper on Dynamo by DeCandia,  Hastorun, et al.

#### Sample Codes & Examples
- [Data Modeling a Gaming Application with Amazon DynamoDB](https://aws.amazon.com/getting-started/projects/data-modeling-gaming-app-with-dynamodb/): A 120-min hands-on lab that looks at a more complex use case of DyanmoDB in gaming. 


