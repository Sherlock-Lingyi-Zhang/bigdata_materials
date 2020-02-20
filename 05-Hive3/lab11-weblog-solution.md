# Lab 11: Log Data Analysis with Hive (solution)

*This lab was recorded earler and some of it no longer corresponds exactly to our latest lab instruction. Please use discretion*

**part 1**

<iframe src="https://www.youtube.com/embed/9c40tXztoLs" width="560" height="315" allowfullscreen="allowfullscreen" allow="autoplay; encrypted-media"></iframe>

**part 2: watch from 6:03 to 12:50**

<iframe src="https://www.youtube.com/embed/X1UpJf6d8oQ" width="560" height="315" allowfullscreen="allowfullscreen" allow="autoplay; encrypted-media"></iframe>

## Step #1: Create and Populate the Web Logs Table

1. Change to the directory for this handsEon exercise: 
    ```
    $ cd $ADIR/exercises/transform
    ```
2. `create_web_logs.hql`
    ```sql
    CREATE EXTERNAL TABLE web_logs (
      ip_address STRING,
      date_string STRING,
      request STRING,
      status STRING,
      bytes STRING,
      referer STRING,
      user_agent STRING,
      cookie STRING
    )
    ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.RegexSerDe'
    WITH SERDEPROPERTIES (
       "input.regex" = "^([\\d.]+) \\S+ \\S+ \\[(.+?)\\] \\\"(.+?)\\\"(\\d{3}) (\\d+) \\\"(.+?)\\\" \\\"(.+?)\\\" \\\"SESSIONID=(\\d+)\\\"\\s*"
    )
    LOCATION '/dualcore/web_logs';
    ```
    Execute the hql file.
    ```bash
    $ beeline -u jdbc:hive2:// -f create_web_logs.hql
    ```
3. Populate the table by adding the log file to the table's directory in HDFS: 

    ```
    $ hadoop fs -mkdir /dualcore/web_logs
    $ hadoop fs -put $ADIR/data/access.log /dualcore/web_logs
    ```
5. Verify that the data is loaded correctly: 
    ```sql
    SELECT term, COUNT(term) AS num FROM
        (SELECT LOWER(REGEXP_EXTRACT(request,
           '/search\\?phrase=(\\S+)', 1)) AS term
           FROM web_logs
           WHERE request REGEXP '/search\\?phrase=') terms
      GROUP BY term
      ORDER BY num DESC
      LIMIT 3;

    -- You should see that it returns tablet (303), ram (153) and wifi (148). 
    ```

    |term | num |
    |-- | -- |
    |tablet|303|
    |ram|153|
    |wifi|148|


## Step #2: Analyze Customer Checkouts

1. Show the number of requests for each step of the checkout process: 

    ```sql
    SELECT COUNT(*), request
    FROM web_logs
    WHERE request REGEXP '/cart/checkout/step\\d.+'
    GROUP BY request;
    ```

    |_c0 | Request |
    |-- | -- |
    |`12955`|`GET /cart/checkout/step1-viewcart HTTP/1.1`|
    |`12552`|`GET /cart/checkout/step2-shippingcost HTTP/1.1`|
    |`8172`|`GET /cart/checkout/step3-payment HTTP/1.1`|
    |`8172`|`GET /cart/checkout/step4-receipt HTTP/1.1`|


2. Create a new table containing the checkout steps completed: 

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

    |steps_completed | num |
    |-- | -- |
    |1|403|
    |2|4380|
    |4|8172|

## Step #3: Extract List of Products Added to Each Cart

1. Write a HiveQL statement to create a table called `cart_items`
    ```sql
     CREATE TABLE cart_items AS
         SELECT cookie, REGEXP_EXTRACT(request, '/cart/additem\\?productid=(\\d+)', 1) AS prod_id
            FROM web_logs
            WHERE request REGEXP '/cart/additem\\?productid=(\\d+)';
    ``` 
3. Verify the contents of the new table: 
    ```sql
    SELECT COUNT(DISTINCT cookie) FROM cart_items WHERE
    prod_id=1273905;
    -- result: 47
    ```




