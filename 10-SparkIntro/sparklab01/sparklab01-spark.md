# Spark Lab 1: Explore RDDs Using the Spark Shell 

### Files and Data Used in this lab

If you're using the Clouder VM:

- Data files (on cloudera VM): `/home/cloudera/training_materials/data/frostroad.txt`

If you're using other VMs:

- [Download a copy of this file ](frostroad.txt)

---

**In this lab you will start the Spark Shell and read a text file into a 
Resilient Distributed Data Set (RDD).**

You may choose to do this lab using either Scala or Python. Follow the   
instructions below for Python, or skip to the next section for Scala.

### Step 1 (Python). Start the Python Spark Shell



1\. Once you ssh into the VM, type `pyspark` in the shell to start PySpark Server. then you can copy the url provided to open it in your MSBA virtual desktop's browser, after replaceing `0.0.0.0` with `localhost`. This will bring up the jupyter notebook. The main purpose of the URL is that it provides a token that allows you to get into pyspark server without using password.

> Please note that, the PySpark use your MSBA virtual desktop's 8888, which will conflict with your local copy of the Jupyter Notebook. In order to access PySpark, you should first shut down the Jupyter Notebook on your MSBA virtual desktop. 

2\. Spark creates a SparkContext object for you called `sc`. Make sure the object exists:

```python
sc
```
> Note: To help you keep track of which shell is being referenced in the
instructions, the prompt will be shown here as either pyspark> or scala>. The
actual prompt will vary depending on which version of Python or Scala you are
using and the command number you are on.

Pyspark will display information about the `sc` object such as
```
<pyspark.context.SparkContext at 0x2724490>
```

3\.  Using command completion, you can see all the available SparkContext methods:  
type `sc`. (`sc` followed by a dot) and then the [TAB] key.  


### Step 1 (Scala). Start and Use the Scala Spark Shell

> Currently, our jupyter notebook does not have a Scala Kernel. So our demonstration here uses the default command command line environment for scala. 
> You can use the nicer Jupyter interface to Scala using a different, lightweight spark VM (that does not have hadoop installed). Please follow the instructions in the computing environment for instructions.

5\. After ssh into the VM, start the Scala Spark Shell by typing:

```
$ spark-shell
```

> You may get several INFO and WARNING messages, which you can disregard. If you don't see the `scala>` prompt after a few seconds, hit Enter a few times t o clear the screen output.

6\. Spark creates a `SparkContext` object for you called sc. Make sure the object exists:

```
scala> sc
```

> Note: To help you keep track of which shell is being referenced in the
instructions, the prompt will be shown here as either pyspark> or scala>. The
actual prompt will vary depending on which version of Python or Scala you are
using and the command number you are on.

Scala will display information about the sc object such as:

```
res0: org.apache.spark.SparkContext =    org.apache.spark.SparkContext@2f0301fa
```

7\.  Using command completion, you can see all the available SparkContext methods:  
type `sc`. (`sc` followed by a dot) and then the [TAB] key.  

### Step 2. Load and view text file (PySpark or Scala)

8\. Review the simple text file you will be using by viewing (without editing) the file in a text editor in a separate window. The file is located at:   
`/home/cloudera/training_materials/data/frostroad.txt`

9\. Define an RDD to be created by reading in the test file on the local file system.  Use the first command if you are using Python, and the second one if you are   
using Scala.    

```
pyspark> mydata = sc.textFile("file:/home/cloudera/training_materials/data/frostroad.txt")
```
```
scala> val mydata = sc.textFile("file:/home/cloudera/training_materials/data/frostroad.txt")
```
> Note : In subsequent instructions, both Python and Scala commands will be  shown but noted explicitly; Python shell commands are preceded  
with pyspark>, and Scala shell commands are in red and preceded with  scala>.

10\. Spark has not yet read the file. It will not do so until you perform an operation on the RDD. Try counting the number of lines in the dataset.

> The count operation causes the RDD to be materialized (created and populated). The number of lines (23) should be displayed, e.g. `Out[4]: 23` (Python) or `res0: 23` (Scala)

11\. Try executing the `collect` operation to display the data in the RDD. Note that this returns and displays the entire dataset. This is convenient for very small RDDs like this one, but be careful using `collect` for more typical large datasets.

12\. Using command completion, you can see all the available transformations and   
operations you can perform on an RDD. Type `mydata`. and then the [TAB] key.

*Lab credits: cloudera*