# Lab 8x: Using CSV SerDe

**lab demonstration (8:48)**

<iframe width="560" height="315" src="https://www.youtube.com/embed/ab3d2HQbBA0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>


1\. Download data to your Cloudera VM.

```shell
# at your home directory
wget http://idsdl.csom.umn.edu/c/share/MSBA6330/titanic.csv
```
2\. Observe the data format

```shell
head titanic.csv
```

3\. Create Hive Managed table in the `default` database.
```sql
create table titanic(
passengerid int,survived int,pclass int,name string,
sex string, age int,sibsp int,parch int,ticket string,
fare string,cabin string,embarked string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar"=",", 
"quoteChar"="\"",
"escapeChar"="\\" 
)
tblproperties ("skip.header.line.count"="1");
```

4\. load data into the table

```sql
-- load data into the table
load data local inpath "/home/cloudera/titanic.csv" into table titanic;
-- query the table
select * from titanic;
```