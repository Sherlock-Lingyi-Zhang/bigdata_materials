
# Lab 6: Running Hive Queries from the Shell, Scripts, and Hue 

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/03-Hive1/lab06-hiveintro/lab06-intro.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

In this lab we will learn different ways of interacting with Hive and 
write HiveQL queries to analyze data in Hive tables.

**Files used in this lab**

> - (table) `dualcore.customers`  (ingested by Sqoop in Lab 2)
> - (table) `dualcore.products`  (ingested by Sqoop in Lab 2)
> - (table) `dualcore.orders`  (ingested by Sqoop in Lab 2)
> - (table) `dualcore.order_details`  (ingested by Sqoop in Lab 2)
> - `$ADIR/exercises/analyzing_sales/verify_tablet_order.hql`

## Preparation 

**IMPORTANT: This lab depends on data produced in Lab 2 via sqoop. To ensure you start with the right data/Hive tables, please run the following command before continuing**: 

```bash
$ ~/scripts/analyst/catchup.sh
# then choose 2: (Using Pig for ETL Processing).
```

Then change the current directory to:
```
$ cd $ADIR/exercises/analyzing_sales
```

## Step #1: Running a Query from the beeline Shell

Dualcore ran a contest in which customers posted videos of interesting ways to use their new tablets. A $5,000 prize will be awarded to the customer whose video received the highest rating. 

However, the registration data was lost due to an RDBMS crash, and the only information we have is from the videos. The winning customer introduced herself only as "Bridget from Kansas City" in her video. 

You will need to run a Hive query that identifies the winner's record in our customer database so that we can send her the $5,000 prize. 

For your reference, you can find the [data model reference](../../faqs/lab_appendix.md) (description of tables and fields) here.



In the next few steps, we will use the beeline to interact with Hive. Keep in mind that to exit beeline, you can type `!exit` or `Ctrl+c`. For more details about beeline commands, you can checkout the [beeline commands documentation](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients#HiveServer2Clients-BeelineCommands).

> Instead of the beeline shell, you may also use the Hive shell, which is older and deprecated. Essentially, you may replace `beeline -u jdbc:hive2://` with  `hive` and get similar results.

1. Start the **beeline** command line environment for Hive: 
    ```bash
    $ beeline -u jdbc:hive2://
    ```
2. As this lab will use the `dualcore` database, set it to be the current database, then display the tables in this database. 
3. Describe the table `customers` to learn about its fields.
4. All you know about the winner is that her name is Bridget and she lives in Kansas City. Use Hive's LIKE operator to do a wildcard search for customers with first names (`fname`) such as "Bridget", "Bridgette" or "Bridgitte". Remember to filter on the customer's city (`city`). 
    **Question** : Which customer did your query identify as the winner of the $5,000 prize? 
5. Exit the beeline shell and return to the command line.

## Step #2: Running a Query Directly from the Command Line



We can submit a query directly from the bash shell using 
```bash
beeline -u jdbc:hive2:// -e 'your_sql_statement(s)'
```
The commands submitted in this way must be quoted. If you have multiple commands, they should be terminated by semicolons (except for the last one). 

You will now run a top-N query to identify the three most expensive products that Dualcore currently offers.  

1. Run the following command to execute the quoted HiveQL statement: 
    ```sql
    SELECT price, brand, name FROM products ORDER BY
    price DESC LIMIT 3
    ```
    **Question**: Which three products are the most expensive? 

## Step # 3 : Running a HiveQL Script

If you already have your SQL statements in a file. You can execute these statements in the file using the `-f` option. 

```bash
beeline -u jdbc:hive2:// -f sql_file.hql
```

The rules for the contest described earlier require that the winner bought the advertised tablet from Dualcore between May 1, 2013 and May 31, 2013. Before we can authorize our accounting department to pay the $5,000 prize, you must ensure that Bridget is eligible. Since this query involves joining data from several tables, it's a perfect case for running it as a Hive script. The script is alread written and saved in `verify_tablet_order.hql` in the current directory.

1. Display the HiveQL code for the query to learn how it works.
2. Note that query references tables in `dualcore` but without the database prefix. Edit the file to add the prefix 
    
    > Recall that a quick way to edit a text file is to use `vi`: `vi filename` to open, `i` to enter edit mode, after making changes, `ESC` to switch to the command mode, `wq` to save and quit.
    
2. Execute the HiveQL script using the beeline command's `-f` option: 

    **Question** : Did Bridget order the advertised tablet in May? 

## Step #4: Running a Query Through Hue and Beeswax

Another way to run Hive queries is through your Web browser using Hue. This is especially convenient if you use more than one computer – or if you use a device (such as a tablet) that isn't capable of running Hive itself – because it does not require any software other than a browser. 

1. On your **Windows virtual desktop**, Type `http://localhost:8888/` into the browser's address bar to connect to Hue. 
    > Alternatively, you can do the same on your cloudera VM in the Firefox browser.   
2. After a few seconds, you should see Hue's login screen. Enter `cloudera` in both the username and password. 
    > Hue integrates many applications. To access Hive, go to `Query browser` in the upper left cornor, then choose Hive. 
3. Select `dualcore` from the database list on the left side of the screen. 
4. Write a query that will count the number of records in the `customers` table, and then click the "Execute" button. 
    
    **Question** : How many customers does Dualcore serve? 
5. Run a query to find the ten states with the most customers. 
    ```sql
    select state, count(*) as cnt from customers group by state order by cnt desc limit 10
    ```
    **Question** : Which state has the most customers? 

*Lab credit: Cloudera, Inc.*

