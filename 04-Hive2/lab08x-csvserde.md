# Lab 8x: Using CSV SerDe

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/04-Hive2/lab08x-csvserde.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

**In this lab, you will practice create Hive Tables using CSV SerDe.** 

**Files used in this lab**

- `titanic.csv`: from here [http://idsdl.csom.umn.edu/c/share/MSBA6330/titanic.csv](http://idsdl.csom.umn.edu/c/share/MSBA6330/titanic.csv)

**Files created in this lab**

- (Hive table) `default.titanic` 

1\. Download data to your Cloudera VM.

```shell
# at your home directory
wget http://idsdl.csom.umn.edu/c/share/MSBA6330/titanic.csv
```
2\. Observe the data format

A description of the dataset can be found at [kaggle website](https://www.kaggle.com/c/titanic/data). For your convenience, we copy the data below:

|Variable|Definition|Key|
| -- | -- | -- |
|passengerid|passenger id||
|survival|Survival|0 = No, 1 = Yes|
|pclass|Ticket class|1 = 1st, 2 = 2nd, 3 = 3rd|
|name|Name||
|sex|Sex||
|Age|Age in years||
|sibsp|# of siblings / spouses aboard the Titanic||
|parch|# of parents / children aboard the Titanic||
|ticket|Ticket number||
|fare|Passenger fare||
|cabin|Cabin number||
|embarked|Port of Embarkation|C = Cherbourg, Q = Queenstown, S = Southampton|

Using linux command `head` to observe a sample of the data. Noting:

- delimiter
- is there quoted fields? if yes, what quote character is used?
- is there a header row?
- is there escaped values (e.g. "," or """)?

3\. Create Hive Managed table in the `default` database.

Noting that, the CSV serde has the following options.
    - the `tblproperties` is not a property of the CSVSerDe but it is commonly used to skip some header lines. 

```sql
CREATE TABLE tablename
(fields...)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
"separatorChar"=",",  -- default: comma separated
"quoteChar"="\"", -- default: use double quotes as quoteChar
"escapeChar"="\\"  -- using \ as escapeChar.
)
tblproperties ("skip.header.line.count"="1"); -- skip 1 header line
```

Mimic the above to create a Hive managed table `titanic` in the default database. For your convenience, you may use the following field definitions. 

```sql
passengerid int,survived int,pclass int,name string,
sex string, age int,sibsp int,parch int,ticket string,
fare string,cabin string,embarked string
```

4\. load data into the table

Load the downloaded data into the table, then query the table to verify that the data is loaded correctly.  


*This is the end of the lab*