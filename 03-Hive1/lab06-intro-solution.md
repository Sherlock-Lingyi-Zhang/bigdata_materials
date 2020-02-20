
# Lab: Running Hive Queries from the Shell, Scripts, and Hue  (solution)

## Preparation

```bash
$ ~/scripts/analyst/catchup.sh
# then choose 2 (Using Pig for ETL Processing) and enter.

$ cd $ADIR/exercises/analyzing_sales
```

## Step #1: Running a Query from the Hive Shell

```bash
# start beeline
$ beeline -u jdbc:hive2://
```
Run these Hive queries in the beeline shell.
```sql
-- set current database
use dualcore;
-- show tables in dualcore
show tables;
-- describe customers
describe customers;
-- look for the winner
select * from customers where fname like "Bridg%" and city = "Kansas City";
-- note that the string comparisons are case sensitive. to make 
-- case insensitive comprisons, use, e.g. lcase(fname) like "bridg%"

-- answer:  Bridget Burtch

!exit --  or ctrl+c

```
## Step #2: Running a Query Directly from the Command Line

```bash
# Which three products are the most expensive? 

$ hive -e 'SELECT price, brand, name FROM dualcore.PRODUCTS ORDER BY price DESC LIMIT 3'

# answer: 
# price   brand   name
# 975149  Byteweasel  Hadoop Cluster, Economy (4-node)
# 614559  Gigabux Server (2U rackmount, eight-core, 64GB, 12TB)
# 599319  Krustybitz  Server (2U rackmount, eight-core, 64GB, 12TB)

```

## Step # 3 : Running a HiveQL Script


```bash
$ cat verify_tablet_order.hql
$ vi verify_tablet_order.hql
    `i`
    add `dualcore.` before all table names.
    `ESC`
    `wq` then enter
$ hive -f verify_tablet_order.hql
# answer: she ordered 2 tablets
```

## Step #4: Running a Hive Query Through Hue

```sql
-- count the number of records in the `customers` tablle
SELECT COUNT(DISTINCT cust_id) AS total FROM customers;
-- note that you cannot omit *, can do count(*) or count(1)
-- answer: 201375

-- Which state has the most customers? 
select state, count(*) as cnt from customers group by state order by cnt desc limit 10

-- state   cnt
-- CA  76278
-- WA  11379
-- AZ  8247
-- IL  7776
-- OR  7719
-- MO  7407
-- MN  6539
-- IA  6514
-- UT  5829
-- ID  5212
```