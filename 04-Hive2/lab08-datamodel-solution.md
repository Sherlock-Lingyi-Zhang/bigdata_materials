# Lab 8: Hive Data Modeling (solution)

**lab demonstration**

Part 1: steps 1-3 (17:32)

<iframe width="560" height="315" src="https://www.youtube.com/embed/M3zQ_Z2AjnM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
Part 2: steps 4 (8:11)

<iframe width="560" height="315" src="https://www.youtube.com/embed/bee7SsJyKcM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
## Step #1: Use Sqoop’s Hive Import Option to Create a Table

1. Change to the directory for this HandsEOn Exercise: 
    ```bash
    $ cd $ADIR/exercises/data_mgmt
    ```
2. Execute the following command to import the suppliers table from MySQL as a new Hive Emanaged table: 
    ```bash
    $ sqoop import \
    --connect jdbc:mysql://localhost/dualcore \
    --username root --password cloudera \
    --fields-terminated-by '\t' \
    --hive-table dualcore.suppliers \
    --table suppliers \
    --hive-import
    ```
4. Validate data by counting the number of suppliers in Texas: 
    ```sql
    SELECT COUNT(*) FROM suppliers WHERE state='TX';
    ```

## Step #2: Create an External Table in Hive

1. Write and execute a HiveQL statement to create an external table for `/dualcore/employees`. 
         
    ```sql
    DROP TABLE IF EXISTS employees;

    CREATE EXTERNAL TABLE employees
       (emp_id STRING,
        fname STRING,
        lname STRING,
        address STRING,
        city STRING,
        state STRING,
        zipcode STRING,
        job_title STRING,
        email STRING,
        active STRING,
        salary INT)
       ROW FORMAT DELIMITED
          FIELDS TERMINATED BY '\t'
          LOCATION '/dualcore/employees';
    ```

2. verify that you have created the table correctly.  
    ```sql
    SELECT job_title, COUNT(*) AS num
    FROM employees
    GROUP BY job_title
    ORDER BY num DESC
    LIMIT 3;
    ```

## Step #3: Create and Load a Hive-Managed Table

1. Create a table named ratings: 
    ```sql  
    DROP TABLE IF EXISTS ratings;

    CREATE TABLE ratings
       (posted TIMESTAMP,
        cust_id INT,
        prod_id INT,
        rating TINYINT,
        message STRING)
       ROW FORMAT DELIMITED
          FIELDS TERMINATED BY '\t';
    ```

2. Show the table description: 

    ```sql
    DESCRIBE ratings;
    ```
3. Populate the table directly by using the `hadoop fs` command: 
    ```bash
    $ hadoop fs -put $ADIR/data/ratings_2012.txt \
    /user/hive/warehouse/ratings
    ```
4. count the number of records in this table (the result should be 464): 

    ```sql
    SELECT COUNT(*) FROM ratings;
    ```
5. Copy the 2013 ratings data to HDFS: 

    ```bash
    $ hadoop fs -put $ADIR/data/ratings_2013.txt /dualcore
    ```
6. Verify that the file is there: 

    ```bash
    $ hadoop fs -ls /dualcore/ratings_2013.txt
    ```
7. **load that file into the ratings table:** 

    ```sql
    LOAD DATA INPATH '/dualcore/ratings_2013.txt' INTO TABLE ratings;
    ```

8. Verify that the file is no longer present in the original directory: 
    ```bash
    $ hadoop fs -ls /dualcore/ratings_2013.txt
    ```
9. Verify that the file is shown alongside the 2012 ratings data in the table’s directory: 

    ```bash
    $ hadoop fs -ls /user/hive/warehouse/ratings
    ```
10. count the records in the `ratings` table to ensure that all 21,997 are available: 

    ```sql
    SELECT COUNT(*) FROM ratings;
    ```
## Step # 4 : Create, Load, and Query a Table with Complex Fields

1. Run the following statement in Hive to create the table: 

    ```sql
    CREATE TABLE loyalty_program
    (cust_id INT,
        fname STRING,
        lname STRING,
        email STRING,
        level STRING,
        phone MAP<STRING, STRING>,
        order_ids ARRAY<INT>,
        order_value STRUCT< min:INT,
                            max:INT,
                            avg:INT,
                            total:INT>)
    ROW FORMAT DELIMITED
        FIELDS TERMINATED BY '|'
        COLLECTION ITEMS TERMINATED BY ','
        MAP KEYS TERMINATED BY ':';

    ```
2. Examine the data in `loyalty_data.txt` then load it into Hive: 

    ```sql
    LOAD DATA LOCAL INPATH '/home/cloudera/training_materials/analyst/exercises/data_mgmt/loyalty_data.txt' 
    INTO TABLE loyalty_program;

    ```
3. Select the `HOME` phone number for customer ID  1200866. 
    ```sql
    from loyalty_program
    select phone['HOME']
    where cust_id=1200866;
    -- 408-555-4914
    ```
4. Select the third element from the `order_ids`. 
    ```sql
    from loyalty_program
    select order_ids[2]
    where cust_id=1200866;
    -- 5278505
    ```
5. Select the `total` attribute. 
    ```sql
    from loyalty_program
    select order_value.total
    where cust_id=1200866;
    -- 401874
    ```

## Bonus Exercise #1: Alter and Drop a Table

```sql
-- 1. Use `ALTER TABLE` to rename the `level` column to `status`. 
ALTER TABLE loyalty_program CHANGE level status STRING;
-- 2. Use the `DESCRIBE` command on the `loyalty_program`. 
DESCRIBE loyalty_program;
-- 3. Use `ALTER TABLE` to rename the entire table to `reward_program`.
ALTER TABLE loyalty_program RENAME TO reward_program;
-- 4. verify this (the result should be "SILVER"): 
SELECT status FROM reward_program WHERE cust_id = 1200866;
-- 5. Drop the `reward_program` table. 
DROP TABLE reward_program;
```
