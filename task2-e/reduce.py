#!/usr/bin/python
import sys

current_medallion = None
current_sum = 0
count = 0
a = {}
for line in sys.stdin:
    
    medallion, value = line.strip().split("\t", 1)
    date, count= value.strip().split(",",1)
        
    
    try:
        count = float (count)
    except ValueError:
        continue
    
    if medallion == current_medallion:
        current_sum += count
         
    else:
        
        if current_medallion:
            
            average = float (current_sum/len(a))
            print ("%s\t%d,%.2f" % (current_medallion, current_sum, average))
            a.clear()
        current_medallion = medallion
        current_sum = float (count)
        average = count
    a[date] = count
        
average = float (current_sum/len(a))
print ("%s\t%d,%.2f" % (current_medallion, current_sum, average))
a.clear()
