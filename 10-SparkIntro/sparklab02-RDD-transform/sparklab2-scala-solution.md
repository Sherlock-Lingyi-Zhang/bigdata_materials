# Spark Lab 2 - Solution (Scala)

## Explore the Loudacre web log files

###  1 
run in bash shell:
```bash
cd $DEV1/exercises/spark-transform

hadoop fs -ls /loudacre/weblogs

hadoop fs -cat /loudacre/weblogs/* | head

spark-shell
```

the rest will run in spark-shell
### 2
```scala
var logfile="/loudacre/weblogs/FlumeData.*"
```
### 3
```scala
var logs = sc.textFile(logfile)
```
### 4
```scala
var jpglogs= logs.filter(line => line.contains(".jpg"))
```
### 5
```scala
jpglogs.take(10)
```
### 6 
```scala
sc.textFile(logfile)
.filter(line => line.contains(".jpg"))
.count()
```
Scala can handle broken long lines automatically

if you give a variable for the above statement, that variable is not RDD, it is a scala variable, you can display it typing its name.

### 7
```scala
logs.map(line => line.length).take(5)
```
### 8
```scala
logs.map(line => line.split(' ')).take(5)
```
### 9
```scala
var ips = logs.map(line =>line.split(' ')(0))
ips.take(5)
```
### 10
```scala
ips.take(10).foreach(println)
```
### 11
```scala
ips.saveAsTextFile("/loudacre/iplist")
```

