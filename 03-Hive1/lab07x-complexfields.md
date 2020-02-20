# Lab 7x: Using Complex Fields in Hive

This lab is designed to get you familiar with defining and using complex fields in Hive. 

The main advantage of complex type is that it allows us to store all information related to an entity in one record, which is very convenient for parallel processing (since such records can be processed independently). Storing data in this format can avoid the use of expensive joins. 

## Step 1: View Complex fields in `customers`

1. In Hue, go to the `default` database, the following statement

```sql
SHOW CREATE TABLE customers;
# SHOW CREATE TABLE  is a way to show the creation statement associated with a table.
```

yields:

```sql 
CREATE TABLE `customers`(
  `id` int, 
  `name` string, 
  -- the next three fields are complex fields.
  `email_preferences` struct<email_format:string,frequency:string,categories:struct<promos:boolean,surveys:boolean>>, 
  `addresses` map<string,struct<street_1:string,street_2:string,city:string,state:string,zip_code:string>>, 
  `orders` array<struct<order_id:string,order_date:string,items:array<struct<product_id:int,sku:string,name:string,price:double,qty:int>>>>)
-- the next three statement has a shorthand: STORED AS PARQUET
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
-- the next statement is equivalent to `LOCATION '/user/hive/warehouse/customers'` in our setting. The `hdfs://quickstart.cloudera:8020` part is the HDFS host URL & port.
LOCATION
  'hdfs://quickstart.cloudera:8020/user/hive/warehouse/customers'
-- the next part is mostly the default values, can be omitted in this case
TBLPROPERTIES (
  'COLUMN_STATS_ACCURATE'='true', 
  'numFiles'='1', 
  'numRows'='0', 
  'rawDataSize'='0', 
  'totalSize'='15812', 
  'transient_lastDdlTime'='1501704658')
```

2. Observe that to define a complex type, we need:

- `struct<member_name:data_type,...>`:e.g., `struct(name:string,age:int)`
- `map<key_type,value_type>`: e.g., `map<string, string>`
- `array<member_type>`: e.g., `array<string>`

Further notice that a complex field can be embedded in a hierarchical structure, as shown in this table.  

## Step 2: Query complex fields

1. To access STRUCT members, you can use dot notation, `structname.membername`. Find all customers who accepts promotional emails.
2. to access MAP members, you can use the square-bracket notation (string index), i.e.,`mapname['member']`. Find all customers who have CA billing addresses and show their name and billing addresses.
3. to access ARRAY members, you can use the square-bracket notation (integer index), i.e.,`arrayname[0]`. In addition, you can use `size()` to find the size of the array. Find all customers who have 2 or more orders, and show their name, number of orders, and the first order's date.
