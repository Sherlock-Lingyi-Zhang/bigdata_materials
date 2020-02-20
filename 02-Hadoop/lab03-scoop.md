
# Lab 3: Importing MySQL Tables into HDFS with Sqoop

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/02-Hadoop/lab03-scoop.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

**In this lab, we use scoop to ingest data from a MySQL database into HDFS.**

**Files used in this lab**

> In the MySQL database `dualcore`:
> ```
> employees
> products
> customers
> orders
> order_details
> ```
> on HDFS
> ```
> /dualcore  (created in lab 1)
> ```

**Directories and files produced by this lab**
> On HDFS
> ```
> /dualcore/employees
> /dualcore/products
> /dualcore/customers
> /dualcore/orders
> /dualcore/order_details
> ```

Dualcore stores information about its employees, customers, products, and orders in a MySQL database. In the next few steps, you will examine this database before using Sqoop to import its tables into HDFS. 

1. Log in to MySQL and select the dualcore database, using one of the following commands: 
    ```bash
    $ mysql -uroot -pcloudera dualcore 
    # or 
    $ mysql --user=root --password=cloudera dualcore
    ```
2. Next, list the available tables in the dualcore database (`mysql>` represents the MySQL client prompt and is not part of the command): 
    ```sql
    mysql>SHOW TABLES; 
    ```
3. Review the structure of the employees table and examine a few of its records: 
    ```sql
    mysql> DESCRIBE employees; 
    mysql> SELECT emp_id, fname, lname, state, salary FROM
    employees LIMIT 10;
    ```
4. Exit MySQL by typing quit, and then hit the enter key: 
    ```sql
    mysql> quit
    ```
> ### Data Model Reference
> For your convenience, you will find a [data model reference](datamodel.pdf) depicting the structure for the tables you will use in the labs.

5. Next, run the following command, which imports the employees table into the `/dualcore` directory created earlier using tab characters to separate each field: 
    ```bash
    $ sqoop import \
    --connect jdbc:mysql://localhost/dualcore \
    --username root --password cloudera \
    --fields-terminated-by '\t' \
    --warehouse-dir /dualcore \
    --table employees
    ```
> ### Hiding Passwords
>
>Typing the database password on the command line is a potential security risk since others may see it. An alternative to using the `--password` argument is to use `-P` and let Sqoop prompt you for the password, which is then not visible when you type it.
>
>### Sqoop Code Generation
>
> After running the sqoop import command above, you may notice a new file named
`employee.java` in your local directory. This is an artifact of Sqoop’s code generation and is really only of interest to Java developers, so you can ignore it.

6. Revise the previous command and import the `customers` table into HDFS. 
7. Revise the previous command and import the `products` table into HDFS. 
8. Revise the previous command and import the `orders` table into HDFS. 
9. Next, you will import the `order_details` table into HDFS. The command is slightly different because this table only holds references to records in the `orders` and `products` table, and lacks a primary key of its own. Consequently, you will need to specify the `--split-by` option and instruct Sqoop to divide the import work among map tasks based on values in the `order_id` field. An alternative is to use the `-m 1` option to force Sqoop to import all the data with a single task, but this would 
significantly reduce performance. 
    ```bash
    $ sqoop import \
    --connect jdbc:mysql://localhost/dualcore \
    --username root --password cloudera \
    --fields-terminated-by '\t' \
    --warehouse-dir /dualcore \
    --table order_details \
    --split-by=order_id
    ```

## This is the end of the lab.

*lab credit: Cloudera, Inc.*
