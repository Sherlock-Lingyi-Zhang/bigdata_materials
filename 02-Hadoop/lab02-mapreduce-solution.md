# Lab 2: Running a Python MapReduce Job (solution)

```bash

# enter the directory
cd $ADIR/exercises/data_ingest/bonus_01
# clean output destination
rm results.txt
hadoop fs -rm -r /user/cloudera/empcounts

# view mapper, reducer, and runjob shell script
cat mapper.py
cat reducer.py
cat runjob.sh
# alternatively, you could do 
vi mapper.py   #`q` to quit
vi reducer.py
vi runjob.sh
# run the mapreduce job.
./runjob.sh

# verify results
hadoop fs -ls /user/cloudera/empcounts
# download the results to a local file
hadoop fs -getmerge /user/cloudera/empcounts results.txt
# view results
less results.txt

```

## Appendix


### mappy.py


```python

#!/usr/bin/env python

import sys

for line in sys.stdin:
   line = line.strip()
   (id, fname, lname, addr, city, state, zip, job, email, active, salary) = line.split("\t")

   if int(salary) >= 75000:
      print "%s,1" % state
```

### mappy.py

```python
#!/usr/bin/env python

import sys

previous_state = ''
count_for_state = 0

for line in sys.stdin:
    line = line.strip()

    (state, number) = line.split(",")

    if state == previous_state:
        count_for_state = count_for_state + int(number)
    else:
        if previous_state != '':
            if count_for_state >= 1:
                print "%s\t%d" % (previous_state, count_for_state)
        previous_state = state
        count_for_state = int(number)

if count_for_state >= 1:
    print "%s\t%d" % (state, count_for_state)
```

### runjob.sh


```bash
#!/bin/sh

# Path of Hadoop streaming JAR library
STREAMJAR=/usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.10.0.jar

# Directory in which we'll store job output
OUTPUT=/user/cloudera/empcounts

# Make sure we don't have output from a previous run.
# The -r option removes the directory recursively, and
# the -f option prevents Hadoop from warning us if the
# directory doesn't exist.
hadoop fs -rm -r -f $OUTPUT

# Run this job
hadoop jar $STREAMJAR \
   -mapper mapper.py -file mapper.py  \
   -reducer reducer.py -file reducer.py  \
   -input /dualcore/employees \
   -output $OUTPUT
```