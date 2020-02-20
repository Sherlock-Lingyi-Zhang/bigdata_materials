# Lab 7: Using HiveQL to Analyze an Advertising Campaign

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/03-Hive1/lab07-hiveql/lab07-hiveql.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.


In this exercise you will write HiveQL queries to analyze data in Hive tables that have been populated with data you placed in HDFS during earlier exercises. The purpose is for you to gain experience with using JOINs, subqueries, and certain string/date functions of Hive. 

**IMPORTANT: This exercise builds on previous ones (including ones that we skipped). Please run the following command to prepare for this exercise before continuing**: 

**Files used in this lab**

> - (table) `dualcore.products`  (ingested by Sqoop in Lab 2)
> - (table) `dualcore.orders`  (ingested by Sqoop in Lab 2)
> - (table) `dualcore.order_details`  (ingested by Sqoop in Lab 2)


This next few steps use the database `Dualcore`.  

Dualcore run an advertising campaign for its tablets (prod_id = 1274348) in May, 2013. The tables `orders` and `order_details` capture the orders placed and what's in each order around that time. The following questions are designed to answer some questions related to the advertising campaign.

## Step 1. Calculating Revenue and Profit

At first, we want to get a sense of overall sales statistics.

Several questions are described below and you will need to write the HiveQL code to answer them. You can use whichever method you like best, including Hive shell, Hive Script, or Hue, to run your queries (we recommend Hue). 

1. Which top three products has Dualcore sold more of than any other? Show `brand`,`name`, and `sold` (count of units sold) in the outcome.
    **Hint** : Remember that if you use a GROUP BY clause in Hive, you must group by all fields listed in the SELECT clause that are not part of an aggregate function. 
2. What was Dualcore’s total revenue in May, 2013? 
3. What was Dualcore’s gross profit (sales price minus cost) in May, 2013? 
4. The results of the above queries are shown in cents. Rewrite the gross profit query to format the value in dollars and cents (e.g., \$2000000.00). To do this, you can divide the profit by 100 and format the result using the `PRINTF` function and the format string  "`$%.2f`". 

## Step #2. Show Per-Month Sales Before and After Campaign

Before we proceed with more sophisticated analysis, you should first calculate the number of orders Dualcore received each month for the three months before our ad campaign began (February – April, 2013), as well as for the month during which our campaign ran (May, 2013). 


1. Write a Hive query to count the number of orders in each of the three months leading to the campaign and the month of the campaign (hint: use `substr` to get the year-month). Display the count by month to the screen. 
    
    **Question** : Does the data suggest that the advertising campaign we started in May led to a substantial increase in orders? 

## Step #3: Count Advertised Product Sales by Month

Our analysis from the previous step suggests that sales increased dramatically the same month we began advertising. Next, you’ll compare the sales of tablets we advertised (product ID #1274348) during the same period to see whether the increase in sales was actually related to our campaign. 

You will be joining two data sets during this portion of the exercise. It is important to keep in mind that an important tip to high-performance queries is to filter out unwanted data from each relation  _before_  you join them. 

1. Write a Hive query to count the number of orders for tablets product in each of the three months leading to the campaign and the month of the campaign (hint: use `substr` to get the year-month) (hint: you need to get month from `orders` and `prod_id` from `order_details`; therefore a join is needed). 
    
    **Question**: Does the data show an increase in sales of the advertised product corresponding to the month in which Dualcore’s campaign was active? 

2. Modify the previous query to do the same for the number of orders for non-advertised products. 
    
    **Question**: Does the data show an increase in sales of the non-advertised product corresponding to the month in which Dualcore’s campaign was active? Why it is important to do this check?    

## Step #4: (Optional Hive Challenge) Calculate Average Order Size

This task is designed to be a challenging task. You may skip it if you want.

It appears that our advertising campaign was successful in generating new orders for Dualcore. Since we sell this tablet at a slight loss to attract new customers, let’s see if customers who buy this tablet also buy other things. You will write code to calculate the average number of items for all orders that contain the advertised tablet during the campaign period. 

1. Write a Hive query to report the average order sizes for the orders in May, 2013 that contains the advertised product. 

    **Question**: Does the data show that the average order contained at least two items in addition to the tablet we advertised? 
    

*Lab credit: Cloudera, Inc.* 
