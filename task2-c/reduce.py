#!/usr/bin/python
import sys

current_passengers = None
current_sum = 0

for line in sys.stdin:
    
    passengers, count = line.strip().split("\t", 1)
    
    try:
        count = int(count)
    except ValueError:
        continue
    
    if passengers == current_passengers:
        current_sum += count
    else:
        if current_passengers:
            print "%s\t%d" % (current_passengers, current_sum)
        current_passengers = passengers
        current_sum = count

print "%s\t%d" % (current_passengers, current_sum)
