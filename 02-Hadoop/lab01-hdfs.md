
# General Notes on Hadoop Labs
**Source code**: [right click on this link](https://github.umn.edu/deliu/bigdata19/blob/master/02-Hadoop/lab01-hdfs.md), open it in a new tab, then right click on the Raw button, save link as, change the file extension to ".md", then save.

The labs in this course is completed using the course Virtual Machine (VM) which runs the CentOS 6.3 Linux distribution. This VM has CDH (Cloudera's Distribution, including Apache Hadoop) installed in pseudo-­‐distributed mode. Pseudo-­‐distributed mode is a method of running Hadoop whereby all Hadoop daemons run on the same machine. It is, essentially, a cluster consisting of a single machine. It works just like a larger Hadoop cluster, the key difference (apart from speed, of course!) is that the block replication factor is set to one, since there is only a single DataNode available.

## Working with the Virtual Machine

1. Should  you  need  it,  the  root  password  is  `cloudera`.  You  may  be  prompted  for this  if,  for  example,  you  want  to  change  the  keyboard  layout.  In  general,  you should not need this password since the `cloudera` user has unlimited sudo rivileges. 

2. In some command-­‐line steps in the labs, you will see lines like this (**DO NOT RUN THIS COMMAND** as this is only an illustration):
    ```
    $ hadoop fs -put shakespeare \
    /user/cloudera/shakespeare
    ```
    > The dollar sign ($) at the beginning of each line indicates the Linux shell prompt. The actual prompt will include additional information (e.g., `[cloudera@localhost workspace]$` ) but this is omitted from these instructions for brevity. 

    > The backslash (`\`) at the end of the first line signifies that the command is not completed, and continues on the next line. You can enter the code exactly as shown (on two lines), or you can enter it on a single line. If you do the latter, you should not type in the backslash.

3.  Although many students are comfortable using UNIX text editors like `vi` or `emacs`, some might prefer a graphical text editor. The graphical text editor is only available when you access the VM through a GUI (via virtualbox). It is not available when we access it from Gitbash or cmd window. If you're in the GUI environment, to invoke the graphical editor from the command line, type `gedit` followed by the path of the file you wish to edit. Appending & to the command allows you to type additional commands while the editor is still open. Here is an example of how to edit a file named `myfile.txt`:

    ```
    $ gedit myfile.txt &
    ```


## Points to Note During the Labs

#### Sample Solutions

If you need a hint or want to check your work, the `sample_solution` subdirectory within each exercise directory contains complete code samples. 

#### Catch up Script

If you are unable to complete an exercise, we have provided a script to catch you up automatically. Each exercise has instructions for running the catch-up script. 

#### `$ADIR` Environment Variable

`$ADIR` is a shortcut that points to the `/home/cloudera/training_materials/analyst` directory, which contains the code and data you will use in Hadoop related labs.  

#### Fewer Step-by-Step Instructions as You Work Through These Exercises

As the exercises progress, and you gain more familiarity with the tools you're using, we  provide fewer step-by-step instructions. You should feel free to ask your instructor for assistance at any time, or to consult with your fellow students. 

---

# Lab 1: Using HDFS

**In this lab you will begin to get acquainted with the Hadoop tools. You will manipulate files in HDFS, the Hadoop Distributed File System.**

**Files used in this lab**

> Data files (local)
> ```
> ~/training_materials/analyst/data/access.log
> ~/training_materials/developer/data/access_log.gz
> ```

**Directories and files produced by this lab**

> On HDFS
> ```
> /dualcore
> /weblog
> /weblog/access_log (file)
> /testlog
> /testlog/test_access_log (file)
> ```

### Step 1: Exploring HDFS

1. Open a terminal window (if one is not already open) by double-clicking the Terminal icon on the desktop. Next, change to the directory for this exercise by running the following command: 
    ```bash
    $ cd $ADIR/exercises/data_ingest
    ```
2. You can use the `hadoop fs` command to interact with the Hadoop Distributed 
Filesystem (HDFS) from the command line. In the terminal window, enter: 
    ```bash
    $ hadoop fs
    ```
    This displays a help message describing all subcommands associated with `hadoop fs`. 
3.  Run the following command:
    ```bash
    hadoop fs -ls / 
    ```
    This command lists the contents of the HDFS root directory. 
    One of the directories listed is `/user`. Each user on the cluster has a 'home' directory below `/user` corresponding to his or her user ID. Since your user ID on the cluster is cloudera, your home directory in HDFS is `/user/cloudera`.
4. List the contents of your home directory (which is currently empty) 
5. If you do not specify a path, `hadoop fs` assumes you are referring to your home directory. Therefore, the following command is equivalent to the one above: (Not working, referred to Cloudera)
    ```bash
    $ hadoop fs -ls
    ```
6. To ensure that the destination HDFS directories are empty. Please run the following to remove the destination directories if they exist. 
    ```bash
    $ hadoop fs -rm -r /dualcore
    $ hadoop fs -rm -r weblog
    $ hadoop fs -rm -r testlog
    ```
7. Most of your work will be in the `/dualcore` directory, so create that now. 
8. Next, add a Web server log file to this new directory in HDFS: 
    ```bash
    $ hadoop fs -put $ADIR/data/access.log /dualcore
    ```
    > ### Overwriting Files in Hadoop
    > Unlike the UNIX shell, Hadoop won't overwrite files and directories. This feature helps protect users from accidentally replacing data that may have taken hours to produce. If you need to replace a file or directory in HDFS, you must first remove the existing one. Please keep this in mind in case you > make a mistake and need to repeat a step during the Hands-On Exercises.
    > 
    > **To remove a file**:
    > ```
    > $ hadoop fs -rm /dualcore/example.txt
    > ```
    > 
    > **To remove a directory (recursively)**:
    > ```
    > $ hadoop fs -rm -r /dualcore/example/
    > ```
9. Verify the last step by listing the contents of the `/dualcore` directory again. You should observe that the access.log file is present and occupies  106,339,468  bytes of space in HDFS: 
10. To practice removing a file, you may now delete the file you just added. 
11. In the following steps, we take a compressed web server log file, uncompress it, and put it in HDFS. This file is currently compressed using GZip. Rather than extract the file to the local disk and then upload it, we will extract and upload in one step. First, create a directory `weblog` in your HDFS **home directory** to store it.
12. Now, extract and upload the file in one step. The `-c` option to gunzip
uncompresses to standard output, and the dash (`-`) in the `hadoop fs -put`
command takes whatever is being sent to its standard input and places that data in HDFS.
    ```bash
    $ gunzip -c ~/training_materials/developer/data/access_log.gz \
    | hadoop fs -put - weblog/access_log
    ```
13. Run the `hadoop fs -ls` command to verify that the log file is in your HDFS home directory.
14. The access log file is quite large – around 500 MB. Create a smaller version of this file, consisting only of its first 5000 lines, and store the smaller version in HDFS. You can use the smaller version for testing in subsequent labs. 
    ```bash
    $ hadoop fs -mkdir testlog
    $ gunzip -c ~/training_materials/developer/data/access_log.gz \
    | head -n 5000 | hadoop fs -put - testlog/test_access_log
    ```



### This is the end of the lab. 

*Lab credit: Cloudera, Inc.*
