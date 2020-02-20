# Lab 2: Running a Python MapReduce Job

**note: this lab requires data produced by lab 3**

**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/02-Hadoop/lab02-mapreduce.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

**This lab is designed to expose you to an example of a MapReduce (streaming) job written in Python**

**Files used in this lab**

> Data files (HDFS)
> ```
> /dualcore/employees  (data ingested by Sqoop in Lab 3)
> ```

**Directories and files produced by this lab**

> ```bash
> # On HDFS
> /user/cloudera/empcounts
> # local
> $ADIR/exercises/data_ingest/bonus_01/results.txt
> ```

Before the lab, to ensure the output directory/files are not there, run the following commands:

```bash
hadoop fs -rm -r /user/cloudera/empcounts
rm $ADIR/exercises/data_ingest/bonus_01/results.txt
```

Dualcore’s Human Resources manager requested that we provide him with the number of employees with salaries of at least $75,000, grouped by state, to help him plan meetings to inform those employees of a recent retirement plan change that affects them.  

A software engineer on our team recently attended Cloudera’s Developer training and was eager to try writing some MapReduce code in Python, so you will briefly examine the code she wrote and then run it to produce the data our HR department requested. 

1. Change to the `bonus_01` subdirectory of the current exercise: 
    ```bash
    $ cd $ADIR/exercises/data_ingest/bonus_01
    ```
2. Examine the MapReduce code for both the mapper and reducer so you can see how it will produce the data we have been asked to provide. 
3. Next, examine the shell script that the software engineer wrote. As you can see, this job defines the path of the Java library (JAR) file that contains support for Hadoop Streaming. It also defines the output directory, making sure that it does not already exist (for example, if a previous job had already created it) before submitting the job for execution on the cluster. 
4. Execute this shell script to run the job. Note that the `./` part of the command is necessary for executing a script in the current directory.  
    ```bash
    $ ./runjob.sh
    ```
    Hadoop should start displaying status messages to your screen within a few seconds, and the job should run for a few minutes before concluding with a message explaining that the output is in the `/user/cloudera/empcounts` directory (in HDFS) and returning control to your terminal. 
5. List the contents of this directory in HDFS. You should see three types of items in this directory: a `_SUCCESS` file indicating that the job completed successfully, a `_logs` directory containing log files from the job (if any were produced), and one or more files whose names start with `part`. These files contain the actual output records created by the job.   
6. Since our job simply produces a small summary of the input data, it would be more convenient to retrieve the contents of the HDFS output directory and merge them into a single file on the local disk. The **`hadoop fs -getmerge`** command does exactly this: 
    ```
    $ hadoop fs -getmerge /user/cloudera/empcounts results.txt
    ```
    The `results.txt` file will not include any data from the `_SUCCESS` file or `_logs` subdirectory in HDFS because this command ignores files whose names begin with an underscore or a period (dot).  
7. Now that this is a local file, you can examine the content of `results.txt`.

If you need help with debugging your MapReduce code, please checkout the tutorials on [how to debug MapReduce](../faqs/debug_hadoop.md) and [how to debug MapReduce Streaming](../faqs/debug_hadoop_streaming.md)

You should now be able to answer the following questions: 

- How many states match the criteria specified by the Human Resources 
department? 
- Which state contains the most employees who match these criteria? (Hint: it is the same state where Dualcore was founded, where the corporate headquarters are located, and where we have the most employees overall.) 

### This is the end of the lab. 

*Lab credit: Cloudera, Inc.*
