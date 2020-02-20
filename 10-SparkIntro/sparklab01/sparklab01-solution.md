# Spark Lab 1 - Solution (PySpark)

## Step 1. Start the Python Spark Shell

1\. start pyspark

```bash
pyspark
```

2\. Make sure SparkContext object exists

```python
sc
```


3\. Use command completion to see all the available SparkContext methodss

if you enter `sc.` and then hit <kbd>tab</kbd> key, you can see a list of `SparkContext` methods.


4\. Exit the shell

In jupyter notebook, you can close the notebook, then choose the running notebook and **Shut down**.

## Step 2. Load and view text file 

9\. Define an RDD by reading a file.

```python
mydata = sc.textFile("file:/home/cloudera/training_materials/data/frostroad.txt")
```
To load a local file, the path should start with "file:/", indicating file is from local (not from HDFS). 

Auto-completion is available in this case, so you can use tab key to complete a path name as you can in Linux shell. Leverage this!


10\. Count the number of lines

```python
mydata.count()
```


11\. Display the **entire** dataset. 

```python
mydata.collect()
```


12\. Command completion.

if you type `mydata.`, then hit <kbd>tab</kbd>, you can see a list of all transformations and operations one can perform on this RDD. type <kbd>Enter</kbd> to see the next screen, type <kbd>q</kbd> to quit 'more'.