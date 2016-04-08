#!/usr/bin/python
import sys

count = 0

for line in sys.stdin:
    
    try:
        line = int(line)
    except ValueError:
        continue
    
    count += line

print "%d" % (count)
