# Lab 11: Log Data Analysis with Hive 

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/05-Hive3/lab11-weblog/lab11-weblog.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

**In this exercise you will create and populate a table with log data from Dualcore's Web server. Queries on that data will reveal that many customers abandon their shopping carts before completing the checkout process. You will learn to create Hive tables based on log data using RegexSerDe. In addition, you use REGEXP_EXTRACT and REGEXP to extract useful information from the log table. You will create several additional tables based on the log data, which you will use later to analyze how Dualcore could turn this problem into an opportunity.**

**IMPORTANT** : This exercise builds on previous ones. If you were unable to complete any  previous exercise or think you may have made a mistake, run the following command to  prepare for this exercise before continuing: 

```bash
$ ~/scripts/analyst/catchup.sh
# then choose 9 (Data Transformation with Hive) 
```

**Files used in this lab**
- (local file) `$ADIR/data/access.log` 

**Files produced by this lab**
- (Hive table) `dualcore.web_logs`
- (Hive table) `dualcore.checkout_sessions`
- (Hive table) `dualcore.cart_items`
- (HDFS) `/dualcore/web_logs/access.log`

## Step #1: Create and Populate the Web Logs Table

Typical log file formats are not delimited, so you will need to use the RegexSerDe and specify a pattern Hive can use to parse lines into individual fields you can then query. 

1. Change to the directory for this handsEon exercise: 

    ```bash
    $ cd $ADIR/exercises/transform
    ```
2. Examine the `create_web_logs.hql` script to get an idea of how it uses a RegexSerDe to parse lines in the log file (an example log line is shown in the comment at the top of the file). When you have examined the script, run it to create the table in Hive 
    > **Note**: add `dualcore.` before the table name `web_logs` so that it will be created in the `dualcore` database; otherwise, you will find the table in the `default` database): 

    ```bash
    $ beeline -u jdbc:hive2:// -f create_web_logs.hql
    ```
3. Populate the table by adding the log file to the table's directory in HDFS: 

    ```bash
    $ hadoop fs -mkdir /dualcore/web_logs
    $ hadoop fs -put $ADIR/data/access.log /dualcore/web_logs
    ```
4. Start the Hive shell in another terminal window 
5. Verify that the data is loaded correctly by running this query to show the top three items users searched for on our Web site: 

    ```sql
    SELECT term, COUNT(term) AS num FROM
        (SELECT LOWER(REGEXP_EXTRACT(request,
           '/search\\?phrase=(\\S+)', 1)) AS term
           FROM web_logs
           WHERE request REGEXP '/search\\?phrase=') terms
      GROUP BY term
      ORDER BY num DESC
      LIMIT 3;
    ```
    You should see that it returns tablet (303), ram (153) and wifi (148). 
    
   >  Note: The `REGEXP` operator, which is available in some SQL dialects, is similar to `LIKE`, but uses regular expressions for more powerful pattern matching. The `REGEXP` operator is synonymous with the `RLIKE` operator. 

## Step #2: Analyze Customer Checkouts

You've just queried the logs to see what users search for on Dualcore's Web site, but now you'll run some queries to learn whether they buy. As on many Web sites, customers add products to their shopping carts and then follow a “checkout” process to complete their purchase. Since each part of this four-step process can be identified by its URL in the logs, we can use a regular expression to easily identify them: 

1. Run the following query in Hive to show the number of requests for each step of the checkout process: 

    ```sql
    SELECT COUNT(*), request
    FROM web_logs
    WHERE request REGEXP '/cart/checkout/step\\d.+'
    GROUP BY request;
    ```

    The results of this query highlight a major problem. About one out of every three customers abandon their cart after the second step. This might mean millions of dollars in lost revenue, so let's see if we can determine the cause. 

2. The log file's `cookie` field stores a value that uniquely identifies each user session. Since not all sessions involve checkouts at all, create a new table containing the checkout steps completed for just those sessions that do: 

    ```sql
    CREATE TABLE checkout_sessions AS
    SELECT cookie, ip_address, COUNT(request) AS steps_completed
    FROM web_logs
    WHERE request REGEXP '/cart/checkout/step\\d.+'
    GROUP BY cookie, ip_address;
    ```
3. Run this query to show the number of people who abandoned their cart after each step: 

    ```sql
    SELECT steps_completed, COUNT(cookie) AS num
    FROM checkout_sessions
    GROUP BY steps_completed;
    ```
    
    You should see that most customers who abandoned their order did so after the second step, which is when they first learn how much it will cost to ship their order.   
    

## Step #3: Extract List of Products Added to Each Cart

From the web-log, you can also obtain a list of items in the customer's cart. You can identify products added to the cart since the request URL looks like this (only the product ID changes from one record to the next): 

```
/cart/additem?productid=1234567
```

1. Write a HiveQL statement to create a table called `cart_items` with two fields: `cookie` and `prod_id` based on data selected from the `web_logs` table. Keep the following in mind when writing your statement: 

    - The `prod_id` field should contain only the seven-digit product ID (hint: use the `REGEXP_EXTRACT` function) 
    - Add a `WHERE` clause with `REGEXP` using the same regular expression as above so that you only include records where customers are adding items to the cart. 
    - If you need a hint on how to write the statement, look at the [lab solution](lab11-weblog-solution.md). 
2. Execute the HiveQL statement from you just wrote. 
3. Verify the contents of the new table by running this query: 

    ```sql
    SELECT COUNT(DISTINCT cookie) FROM cart_items WHERE
    prod_id=1273905;
    ```

    If this doesn't return 47, then compare your statement to the solution, make the necessary corrections, and then re-run your statement (after dropping the `cart_items` table). 

## Next steps

This lab stops here, but there are more that you can do with Hive to continue the shopping cart abandonment analysis. For example,

- infer the zip-code based on the IP address (with help of external scripts)
- estimate the shipping costs based on item weights (by joining `products` and `cart_items` tables and use the zip-code information)
- recover the total selling price and the total wholesale costs.

The information recovered here can also be fed into machine learning models for further analysis. 

**This is the end of the Lab**

*Lab Credit: Cloudera, Inc.* 