#!/usr/bin/python
import sys

current_fare = None
current_sum = 0

for line in sys.stdin:
    
    fare, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if fare == current_fare:
        current_sum += count
    else:
        if current_fare:
            print "%s\t%d" % (current_fare, current_sum)
        current_fare = fare
        current_sum = count

print "%s\t%d" % (current_fare, current_sum)
