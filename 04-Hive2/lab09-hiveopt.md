# Lab 9: Hive Optimization

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/04-Hive2/lab09-hiveopt/lab09-hiveopt.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

**In this exercise, you will practice techniques to improve Hive query performance.**

**IMPORTANT:** Use a single session of Beeline or Hue’s Hive Query Editor to complete all the steps of this exercise. Except for this one session, close all other sessions of Beeline and close all other web browser windows containing Hue’s Hive Query Editor.

## Preparation

1. Create a new directory `hive_optimization` under `$ADIR/exercises/`. Use this new directory as your working directory
2. Download the dataset `movie.zip` using a utility `wget`
    ```bash
    wget http://idsdl.csom.umn.edu/c/share/msba6330/movie.zip
    ```
3. Create a Hadoop directory `/user/cloudera/movies`:
4. Unzip the file and put into the above-created hadoop directory as a new file `movie.text`. You can combine the unzip and put steps using pipe. We did something similar in [Lab 1's step 11](../../../02-hadoop/lab01-hdfs/lab01-hdfs-solution.md), except that `gunzip -c` should be replaced by `unzip -p` here.

## Step #1: Using Hive with Hadoop Standalone Mode

Dualcore sells 1,114 different products representing 47 different brands. The
Marketing Director needs your help to identify which brands have the largest numbers of products, so that advertising campaigns can be planned to increase customer awareness of these brands.

You may use either Beeline or Hue’s Hive Query Editor to complete these exercises.

1. The following Hive query returns the top 10 brands as measured by the number of products for sale. Paste this HiveQL into Beeline or Hue’s Hive Query Editor and execute the query:
    ```sql
    SELECT brand, COUNT(prod_id) AS num
    FROM products
    GROUP BY brand
    ORDER BY num DESC
    LIMIT 10;
    ```
2. Observe the amount of time the query takes to complete.
3. View Hive’s execution plan by prefixing your query with EXPLAIN or by using the **Explain** button in Hue. Observe that the Hive query executes as a MapReduce job that includes both a map phase and reduce phase.
4. Because this query processes a very small amount of data (the products table
contains 1,114 rows and its data is about 60kb in size), a large proportion of the query’s running time is consumed by the overhead of the MapReduce job. Because the data is small, we can reduce this overhead by using Hadoop standalone mode to run the query in a single Java Virtual Machine (JVM) on the Hive Server. Enable standalone mode by issuing the Hive command:
    ```sql
    SET mapreduce.framework.name=local;
    ```
5. Now execute the same Hive query that was executed in the first step of this exercise again, and observe the amount of time the query takes to complete.
6. In preparation for running other queries on larger datasets, switch back to using distributed mode by issuing the Hive command:
    ```sql
    SET mapreduce.framework.name=yarn;
    ```

## Step #2: Using Hive on Spark

Due to limitation of our VM, **we will skip this.** But if you would have Hive-on-spark enable, you can activate it by running the following Hive command:

```sql
#  SET hive.execution.engine=spark; (Don't run it)
```

## Step #3: Using the ORC storage format.

ORC format speeds up Hive query by compressing data and taking advantage of columnar storage format, among others. 

1. Let us first create a database `movies`, then create an External hive table `movie_raw` in this database using the data in `/user/cloudera/movies/` with the following fields. Before creating the table, be sure to view a sample of the data (e.g. determining the delimiter). After creating the table, verify its content using `select * from movie_raw limit 10`.

    |field|type|
    |--|--|
    |id|INT|
    |name|STRING|
    |year|INT|


2. Now create a hive-managed ORC table `movie_orc` for the same data. 
    ```sql
    CREATE TABLE movies.movie_orc (
        id INT,
        name STRING,
        year int
        ) STORED AS ORC;
    ```
3. We don't have data already in the ORC format that we can upload. However, we can use Hive's `INSERT INTO ... SELECT` statement to create data in such a format, using `movie_raw` as a data source.
    ```sql
    INSERT INTO TABLE movie_orc 
    SELECT *
    FROM movie_raw;
    ```
4. Let us compare the files on disk for the two tables, using `hadoop fs -du -h`. `du` is a disk utility. The `-h` option gives you a human-friendly format.
    ```bash
    $ hadoop fs -du -h some_path
    ```

5. We expect that the smaller file sizes lead to increased query performance. However, in this case, because the dataset size is quite small, the difference may not be significant enough to affect the overall execution time. Still, you may use the following queries to do a performance comparison.
    ```sql
    select year, count(*) from movie_raw group by year;
    select year, count(*) from movie_orc group by year;
    ```

## Step #4: Using partitioned tables to improve query performance.



Another optimization strategy is to use partitioned tables. Which column should we use as partition column? We can quickly rule out `id`, and `name` column because of their high cardinality. What about year? One can argue that year is too fine grained too - as it seems too excessive to create a folder for each year. A more reasonable approach is to partition it based on decades, assuming that users use `decade` as a filter often.

1. First create a new managed table  `movie_orc_partitioned` with `decade` being the partition field. We still use ORC as the storage format.
    ```sql
    CREATE TABLE movies.movie_orc_partitioned (
        id INT,
        name STRING,
        year INT
    ) partitioned by (decade int) STORED AS ORC;
    ```
    > Note that the table has `decade` as a virtual field.
2. Partitioned tables require special loading. Loading data partition by partition may be too tedious as there are dozens of decades. We can also load data using dynamic partitioning. First run
    ```sql
    SET hive.exec.dynamic.partition.mode = nonstrict;
    ```
    This allows us to treat `decade` as a dynamic partition column. In the strict mode, at least one static partition column needs to be there. 
3. Loading data into `movie_orc_partitioned`. We don't have decade in the existing data, but we can calculate it:
    ```sql
    INSERT INTO TABLE movies.movie_orc_partitioned PARTITION(decade) 
    SELECT id,name,year, floor(year/10)*10
    FROM movies.movie_orc;
    ```
4. Compare the performance of the following two queries. 
    ```sql
    select count(*) from movie_orc where floor(year/10)*10=1950;
    select count(*) from movie_orc_partitioned where decade=1950;
    ```

## Step 5: Bucketing

In this section, we practice creating and using a bucketed table.

1\. First create a Hive managed table `movie_bucketed` based on the `id` column. Set it to use 10 buckets.

2\. In order to enable bucketing, we first need to set the following option (otherwise, you could end up with just one bucket):
```sql
SET hive.enforce.bucketing=true;  
```
Then insert data into `movie_bucketed` by selecting data from `movie_orc`.

3\. Verify buckets by examining the files/directories in the Hive warehouse. You also verify the # of rows in each bucket to see if they're evenly distributed. You also inspect the IDs in each bucket to see if they appear random. 

4\. Query table using buckets. Count the number of rows in a 40% sample of the the data using the buckets (`TABLESAMPLE (BUCKET 2 OUT OF 5 ON id)`)

*This is the end of the lab*