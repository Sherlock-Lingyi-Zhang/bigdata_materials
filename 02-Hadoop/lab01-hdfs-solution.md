
# Lab 1: Using HDFS and MapReduce


```bash
# Next, change to the directory for this lab
cd $ADIR/exercises/data_ingest
# displays a help message describing all subcommands associated with `hadoop fs`
hadoop fs
# lists the contents of the HDFS root directory
hadoop fs -ls /
# clean up destinations before we start.
hadoop fs -rm -r /dualcore
hadoop fs -rm -r weblog
hadoop fs -rm -r testlog
# create a `/dualcore` directory
hadoop fs -mkdir /dualcore
# add a Web server log file to this new directory
hadoop fs -put $ADIR/data/access.log /dualcore
# Verify the last step by listing the contents of the `/dualcore` directory
hadoop fs -ls /dualcore
# to remove the file just added
hadoop fs -rm /dualcore/access.log
# create a directory weblog in your home directory on HDFS
hadoop fs -mkdir weblog
# unzip and upload access_log.gz
gunzip -c ~/training_materials/developer/data/access_log.gz | hadoop fs -put - weblog/access_log
# verify the log file
hadoop fs -ls weblog
# save the first 5000 lines in testlog/test_access_log
hadoop fs -mkdir testlog
gunzip  -c ~/training_materials/developer/data/access_log.gz | head -n 5000 | hadoop fs -put - testlog/test_access_log  

```
