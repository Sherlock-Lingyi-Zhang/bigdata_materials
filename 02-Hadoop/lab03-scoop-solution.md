# Lab 3: Importing MySQL Tables into HDFS with Sqoop (solution)

```bash
mysql -uroot -pcloudera dualcore 

mysql> SHOW TABLES;
mysql> DESCRIBE employees;
mysql> SELECT emp_id, fname, lname, state, salary FROM
mysql> employees LIMIT 10;
mysql> quit


# import employees
sqoop import \
--connect jdbc:mysql://localhost/dualcore \
--username root --password cloudera \
--fields-terminated-by '\t' \
--warehouse-dir /dualcore \
--table employees

# import customers
sqoop import \
--connect jdbc:mysql://localhost/dualcore \
--username root --password cloudera \
--fields-terminated-by '\t' \
--warehouse-dir /dualcore \
--table customers

# import products
sqoop import \
--connect jdbc:mysql://localhost/dualcore \
--username root --password cloudera \
--fields-terminated-by '\t' \
--warehouse-dir /dualcore \
--table products

# import orders
sqoop import \
--connect jdbc:mysql://localhost/dualcore \
--username root --password cloudera \
--fields-terminated-by '\t' \
--warehouse-dir /dualcore \
--table orders

# import order_details
sqoop import \
--connect jdbc:mysql://localhost/dualcore \
--username root --password cloudera \
--fields-terminated-by '\t' \
--warehouse-dir /dualcore \
--table order_details \
--split-by=order_id


***************
--columns cust_id, name, address, date, history, occupation  
--where item>=1234 

--hive-import

```

