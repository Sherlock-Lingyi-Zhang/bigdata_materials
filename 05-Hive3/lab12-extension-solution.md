# Lab 12: Work with JSON documents and External Scripts in Hive

## Working with Json Documents

1\. Modify the following query to find the name of the price of bicycle. 

```sql
select get_json_object('{"store": {"fruit":[{"weight":8,"type":"apple"},{"weight":9,"type":"pear"}],"bicycle":{"price":19.95,"color":"red"}}, "email":"amy@only_for_json_udf_test.net", "owner":"amy"}'
,'$.store.bicycle.price');
```

2\. Modify the above query to find the name of the first fruit in the store's fruit list. 

```sql
select get_json_object('{"store": {"fruit":[{"weight":8,"type":"apple"},{"weight":9,"type":"pear"}],"bicycle":{"price":19.95,"color":"red"}}, "email":"amy@only_for_json_udf_test.net", "owner":"amy"}'
,'$.store.fruit[0].type');
```

## Working with JSON tables

1\. Download the JSON serde jar file to your home directory.

```shell
cd ~
wget http://idsdl.csom.umn.edu/c/share/msba6330/json-serde-1.3.8-jar-with-dependencies.jar
```

2\. In Hive, run 

```sql
ADD JAR /home/cloudera/json-serde-1.3.8-jar-with-dependencies.jar;
```

3\. Extract a sample row from one of the document and inspect it. 

```shell
cd ~/training_materials/data/chatlogs
head -1 2014-03-15.json
```

4\. Create a Hive managed table `conversations` in Hive to match with the JSON structure, using the JSON Serde. 

```sql
create table conversations (
	conversationId INT,
	accountNum INT,
	agentName STRING,
	category STRING,
	messages ARRAY<STRUCT<sender:STRING, time:TIMESTAMP, text:STRING>>
) 
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe';
```

5\. Load the last file from `/home/cloudera/training_materials/data/chatlogs` -- 2015 2014-03-15.json -- into `conversations`.

```
load data local inpath '/home/cloudera/training_materials/data/chatlogs/2014-03-15.json' 
into table conversations;
```

6\. Verify data by checking:

```sql
select count(*) from conversations;
-- 2980
select * from conversations limit 5;
select conversationid, size(messages) from conversations limit 10;
```

## Testing a transform script

3\. Download a python script `greeting.py` from [http://idsdl.csom.umn.edu/c/share/msba6330/greeting.py](http://idsdl.csom.umn.edu/c/share/msba6330/greeting.py).

```shell
wget http://idsdl.csom.umn.edu/c/share/msba6330/greeting.py
```
<!-- chmod +x greeting.py -->

4\. Upload `greeting.py` to HDFS's `/user/cloudera/greeting.py`

```shell
hadoop fs -put greeting.py greeting.py
```

5\. In Hue, create the table `employees` in the `default` database. 

```sql
create table employees (name string, email string)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
```

6\. In Hue, add a new text file for the `employees` table, with the following data.

```shell
Antoine,antoine@example.fr
Kai,kai@example.de
Pedro,pedro@example.mx
Joel,joel@example.us
```
You can do this either using the text editor from the file browser or run the following HiveQL command:

```sql
INSERT INTO table employees 
values 
("Antoine","antoine@example.fr"),
("Kai","kai@example.de"),
("Pedro","pedro@example.mx"),
("Joel","joel@example.us");
```

7\. In Hue, add the greeting.py file.

```sql
add file hdfs:///user/cloudera/greeting.py;
```

8\. Use the customer script to obtain the personalized greetings. 

```sql
SELECT TRANSFORM(name,  email)
    USING 'greeting.py' AS greeting
    FROM employees;
```

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
        print "{0}\t{1}".format(greetings[match.group(1)],name)
    else:
        print "Hello\t{0}".format(name)
```