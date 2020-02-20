# Lab 8: Hive Data Modeling 

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/04-Hive2/lab08-datamodel/lab08-datamodel.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.


**In this exercise you will practice using several common techniques for creating and populating Hive tables.** 

**IMPORTANT**: This exercise builds on previous ones. If you were unable to complete any previous exercise or think you may have made a mistake, run the following command to prepare for this exercise before continuing: 

```bash
$ ~/scripts/analyst/catchup.sh
# then choose 2: (Using Pig for ETL Processing).
```

**Additionally, many of the shell commands you will run use environmental variables and relative file paths. If you use beeline shell for hive, you may use these as well. However, to run similar queries in Hue, you must use absolute paths and must not use these environment variables.** 

**Files used in this lab**

- (MySQL table) `dualcore.suppliers` 
- (HDFS) `/dualcore/employees` (ingested by Sqoop in Lab 2)
- (local file) `$ADIR/data/ratings_2012.txt`
- (local file) `$ADIR/data/ratings_2013.txt`
- (local file) `$ADIR/exercises/data_mgmt/loyalty_data.txt`

**Files created in this lab**

- (Hive table) `dualcore.suppliers` 
- (Hive table) `dualcore.employees`
- (Hive table) `dualcore.ratings`
- (Hive table) `dualcore.loyalty_program`

## Step #1: Use Sqoop’s Hive Import Option to Create a Table

You used Sqoop in an earlier exercise to import data from MySQL into HDFS. Sqoop can also create a Hive table with the same fields as the source table in addition to importing the records, which saves you from having to write a `CREATE TABLE` statement. 

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
3. Start Hue at http://localhost:8888 on your windows virtual desktop. Then choose `dualcore` as your current database. 
4. It is always a good idea to validate data after adding it. Execute the Hive query shown below to count the number of suppliers in Texas: 
    ```sql
    SELECT COUNT(*) FROM suppliers WHERE state='TX';
    ```
    The query should show that nine records match. 

## Step #2: Create an External Table in Hive

You imported data from the employees table in MySQL in an earlier exercise, but it would be convenient to be able to query this from Hive. Since the data already exists in HDFS, this is a good opportunity to use an external table.  

1. Write and execute a HiveQL statement to create an external table for the tab-delimited records in HDFS at `/dualcore/employees`. The data format is shown below: 
     
    |Field Name | Field Type|
    |--|--|
    |emp_id  |`STRING`|
    |fname  |`STRING`|
    |lname  |`STRING`|
    |address  |`STRING`|
    |city  |`STRING`|
    |state  |`STRING`|
    |zipcode  |`STRING`|
    |job_title  |`STRING`|
    |email  |`STRING`|
    |active  |`STRING`|
    |salary  |`INT`|

2. Run the following Hive query to verify that you have created the table correctly.  
    ```sql
    SELECT job_title, COUNT(*) AS num
    FROM employees
    GROUP BY job_title
    ORDER BY num DESC
    LIMIT 3;
    ```
    It should show that Sales Associate, Cashier, and Assistant Manager are the three most common job titles at Dualcore. 


## Step #3: Create and Load a Hive-Managed Table

Next, you will create and then load a Hive-managed table with product ratings data. 

1. Create a table in the **`default`** database named `ratings` for storing tab-delimited records using this structure: 
  
    |Field Name | Field Type|
    |--|--|
    |posted  |`TIMESTAMP`|
    |cust_id  |`INT`|
    |prod_id  |`INT`|
    |rating  |`TINYINT`|
    |message  |`STRING`|

2. Show the table description and verify that its fields have the correct order, names, and types: 

    ```sql
    DESCRIBE ratings;
    ```
3. Next, open a separate terminal window so you can run the following shell command. This will populate the table directly by using the `hadoop fs` command to copy product ratings data from 2012 to that directory in HDFS: 
    ```bash
    $ hadoop fs -put $ADIR/data/ratings_2012.txt \
    /user/hive/warehouse/ratings
    ```

    Leave the window open afterwards so that you can easily switch between Hive and the command prompt. 

4. Next, verify that Hive can read the data we just added. Run the following query in Hive to count the number of records in this table (the result should be 464): 

    ```sql
    SELECT COUNT(*) FROM ratings;
    ```

5. Another way to load data into a Hive table is through the `LOAD DATA` command. The next few commands will lead you through the process of copying a local file to HDFS and loading it into Hive. First, copy the 2013 ratings data to HDFS: 

    ```bash
    $ hadoop fs -put $ADIR/data/ratings_2013.txt /dualcore
    ```
6. Verify that the file is there: 

    ```bash
    $ hadoop fs - ls /dualcore/ratings_2013.txt
    ```
7. Use the `LOAD DATA` statement in Hive to load that file into the ratings table: 
    ```sql
    LOAD DATA INPATH '/dualcore/ratings_2013.txt' INTO TABLE ratings;
    ```

8. The `LOAD DATA INPATH` command  _moves_  the file to the table’s directory. Verify that the file is no longer present in the original directory: 
    ```bash
    $ hadoop fs -ls /dualcore/ratings_2013.txt
    ```
9. Verify that the file is shown alongside the 2012 ratings data in the table’s directory: 

    ```bash
    $ hadoop fs -ls /user/hive/warehouse/ratings
    ```
10. Finally, count the records in the ratings table to ensure that all 21,997 are available: 

    ```sql
    SELECT COUNT(*) FROM ratings;
    ```
## Step # 4 : Create, Load, and Query a Table with Complex Fields

Dualcore recently started a loyalty program to reward our best customers. A colleague has already provided us with a sample of the data that contains information about customers who have signed up for the program, including their phone numbers (as a map), a list of past order IDs (as an array), and a struct that summarizes the minimum, maximum, average, and total value of past orders. You will create the table, populate it with the provided data, and 
then run a few queries to practice referencing these types of fields. 


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
2. Examine the data in `loyalty_data.txt` to see how it corresponds to the fields in the table and then load it into Hive: 

    ```sql
    LOAD DATA LOCAL INPATH 'loyalty_data.txt' INTO TABLE
    loyalty_program;
    -- when running this in Hue, use the absolute path 
    -- `/home/cloudera/training_materials/analyst/exercises/data_mgmt/loyalty_data.txt`
    ```
3. Run a query to select the `HOME` phone number (hint: map keys are case-sensitive) for customer ID  1200866. You should see  408-555-4914  as the result. 
4. Select the third element from the `order_ids` array for customer ID  1200866 (hint: elements are indexed from zero). The query should return  5278505. 
5. Select the `total` attribute from the `order_value` struct for customer ID 1200866. The query should return 401874. 

## Bonus Exercise #1: Alter and Drop a Table

If you have successfully finished the main exercise and still have time, feel free to continue with this bonus exercise. 

1. Use `ALTER TABLE` to rename the `level` column to `status`. 
2. Use the `DESCRIBE` command on the `loyalty_program` table to verify the change. 
3. Use `ALTER TABLE` to rename the entire table to `reward_program`. 
4. Although the `ALTER TABLE` command often requires that we make a corresponding change to the data in HDFS, renaming a table or column does not. You can verify this by running a query on the table using the new names (the result should be "SILVER"): 

    ```sql
    SELECT status FROM reward_program WHERE cust_id = 1200866;
    ```
5. As sometimes happens in the corporate world, priorities have shifted and the program is now canceled. Drop the `reward_program` table. 

### This is the end of the lab

*Lab Credit: Cloudera, Inc.*