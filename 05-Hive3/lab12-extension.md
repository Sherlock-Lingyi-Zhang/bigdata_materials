# Lab 12: Work with JSON documents and External Scripts in Hive

## Working with JSON Documents

1\. Modify the following query to find the name of the price of bicycle. 

```sql
select get_json_object('{"store": {"fruit":[{"weight":8,"type":"apple"},{"weight":9,"type":"pear"}],"bicycle":{"price":19.95,"color":"red"}}, "email":"amy@only_for_json_udf_test.net", "owner":"amy"}'
,'_____');
```

2\. Modify the above query to find the name of the first fruit in the store's fruit list. 

```sql
select get_json_object('{"store": {"fruit":[{"weight":8,"type":"apple"},{"weight":9,"type":"pear"}],"bicycle":{"price":19.95,"color":"red"}}, "email":"amy@only_for_json_udf_test.net", "owner":"amy"}'
,'______');
```

## Working with JSON tables.

Our VM has some JSON documents at `/home/cloudera/training_materials/data/chatlogs`. These are call logs saved in JSON document. 

Because our VM has not JSON serde installed by default, we need to download and install json serde ourselves (the same steps can be used for installing other customer serdes). First we download the jar file. The original file is at [https://docs.aws.amazon.com/athena/latest/ug/json.html#openxjson](https://docs.aws.amazon.com/athena/latest/ug/json.html#openxjson). For convenience, we have make it available at [http://idsdl.csom.umn.edu/c/share/msba6330/json-serde-1.3.8-jar-with-dependencies.jar](http://idsdl.csom.umn.edu/c/share/msba6330/json-serde-1.3.8-jar-with-dependencies.jar).

1\. Download the JSON serde jar file to your home directory.

```shell
cd ~
wget http://idsdl.csom.umn.edu/c/share/msba6330/json-serde-1.3.8-jar-with-dependencies.jar
```

2\. In Hive, run 

```sql
ADD JAR /home/cloudera/json-serde-1.3.8-jar-with-dependencies.jar;
```

Note that the path is interpreted as your local host path. 


3\. Extract a sample row from one of the document and inspect it. Make sure that it does meet the criteria for a JSON table: i.e. each table row is a JSON object in one line. 


4\. Create a Hive managed table `conversations` in Hive to match with the JSON structure, using the JSON Serde. 


5\. Load the last file from `/home/cloudera/training_materials/data/chatlogs` -- 2015 2014-03-15.json -- into `conversations`.


6\. Verify data by checking:

- number of rows in the table
- first 5 rows
- first 10 rows, reporting conversationid and the number of messages. 


## Testing a transform script

3\. Download a python script `greeting.py` from [http://idsdl.csom.umn.edu/c/share/msba6330/greeting.py](http://idsdl.csom.umn.edu/c/share/msba6330/greeting.py); use `wget` if you use a command line.

4\. Upload `greeting.py` to HDFS's `/user/cloudera/greeting.py`

5\. In Hue, create the table `employees` in the `default` database with two fields, `name` and `email`, fields delimited by ",". 

6\. Inser the following data into the `employees` table.

```
Antoine,antoine@example.fr
Kai,kai@example.de
Pedro,pedro@example.mx
Joel,joel@example.us
```

7\. In Hue, add the greeting.py file.

```sql
add file hdfs:///user/cloudera/greeting.py;
```

8\. Use the customer script to obtain the personalized greetings.

## Appendix: greeting.py

```python
#!/usr/bin/env python
import sys
import re
greetings  = {'de':'Hallo','fr':'Bonjour','mx':'Hola'}

for line in sys.stdin:
    name, email = line.strip().split('\t')
    match = re.search(r'\.(\w+)', email)
    if match and greetings.has_key(match.group(1)):
        print "{0}, {1}".format(greetings[match.group(1)],name)
    else:
        print "Hello, {0}".format(name)
```
**This is the end of the Lab**
