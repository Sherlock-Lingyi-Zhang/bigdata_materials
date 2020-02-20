# Lab: Hive Optimization (solution)

**lab demonstration (8:48)**

Part 1 - Using Faster Engines / Storage (16:47)

<iframe width="560" height="315" src="https://www.youtube.com/embed/_u3Hf-blJmk" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

Part 2 - Partitioning (10:20)

<iframe width="560" height="315" src="https://www.youtube.com/embed/4omHrZTvmXM" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

## Preparation


```bash
# create directory
cd $ADIR/exercises/
mkdir hive_optimization
cd hive_optimization

#download ata
wget http://idsdl.csom.umn.edu/c/share/msba6330/movie.zip

# Create a Hadoop directory `/user/cloudera/movies`:
hadoop fs -mkdir /user/cloudera/movies
# unzip data and put into HDFS
unzip -p movie.zip | hadoop fs -put - /user/cloudera/movies/movie.txt
```

## Using Hive with Hadoop Standalone Mode


1. Run query
    ```sql
    SELECT brand, COUNT(prod_id) AS num
    FROM products
    GROUP BY brand
    ORDER BY num DESC
    LIMIT 10;
    ```
4. Enable local mode
    ```sql
    SET mapreduce.framework.name=local;
    ```
6. Restore mapreduce mode
    ```sql
    SET mapreduce.framework.name=yarn;
    ```


## Using ORC storage format.

1. Create database & table
    ```sql
    create database movies;

    CREATE EXTERNAL TABLE movies.movie_raw (
        id INT,
        name STRING,
        year int
        ) ROW FORMAT DELIMITED  FIELDS TERMINATED BY '|' LOCATION '/user/cloudera/movies/';

    ```

2. Now create a hive-managed ORC table `movie_orc`. 
    ```sql
    CREATE TABLE movies.movie_orc (
        id INT,
        name STRING,
        year int
        ) STORED AS ORC;
    ```
6. Load data into the orc table.
    ```sql
    INSERT INTO TABLE movie_orc 
    SELECT *
    FROM movie_raw;
    ```
7. Compare disk space
    ```bash
    $ hadoop fs -du -h /user/cloudera/movies
    43.6 M  43.6 M  /user/cloudera/movies/movie.txt
    $  hadoop fs -du -h /user/hive/warehouse/movies.db
    15.9 M  15.9 M  /user/hive/warehouse/movies.db/movie_orc
    ```
    > You need to know where things are on Hive. Because `movie_raw` is an External table, it is at where we upload the data, i.e. '/user/cloudera/movies/'. `movie_orc` on the other hand, is a Hive managed table. By default it will be stored in `/user/hive/warehouse/dbname.db/`. If you are not sure, use "describe formatted tablename" to find out. You should find ORC leads to significant smaller file sizes. Why the difference?

8. Performance comparison
    ```sql
    select year, count(*) from movie_raw group by year;
    select year, count(*) from movie_orc group by year;
    ```

## Using partitioned tables to improve query performance.

1. Create partitioned table
    ```sql
    CREATE TABLE movies.movie_orc_partitioned (
        id INT,
        name STRING,
        year INT
    ) partitioned by (decade int) STORED AS ORC;
    ```
2. Enable nonstrict dynamic partitioning.
    
    ```sql
    SET hive.exec.dynamic.partition.mode = nonstrict;
    ```
3. Loading data into `movie_orc_partitioned`.     
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

## Bucketing

1\. Create table:

```sql
CREATE TABLE movie_bucketed  (id INT,
     name STRING,
     year INT)
CLUSTERED BY (id) INTO 10 BUCKETS;
```

2\. Enable bucketing and insert records

```sql
SET hive.enforce.bucketing=true;  

INSERT OVERWRITE TABLE movie_bucketed 
   SELECT * FROM movie_orc;
```

3\. Verify buckets created.

```shell
hadoop fs -ls /user/hive/movies.db/movie_bucketed/

# you may also examine # of lines in each bucket.
hadoop fs -cat /user/hive/movies.db/movie_bucketed/000000_0/*  | wc -l
hadoop fs -cat /user/hive/movies.db/movie_bucketed/000000_1/*  | wc -l
```

4\. Query table using buckets.

```sql
SELECT count(*) FROM orders_bucketed
TABLESAMPLE (BUCKET 2 OUT OF 5 ON order_id);
```
