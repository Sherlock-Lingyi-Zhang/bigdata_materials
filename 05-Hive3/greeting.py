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