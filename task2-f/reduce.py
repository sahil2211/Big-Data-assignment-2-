#!/usr/bin/python
import sys

current_medallion = None
current_license = None
current_sum = 0
a = {}
for line in sys.stdin:
    
    license, medallion = line.strip().split("\t", 1)

    
        
    if license != current_license:
        if current_license:
            print ("%s\t%d" % (current_license, len(a)))
            a.clear()
        current_sum = 1

        current_license = license
    
    a[medallion] = 1

print ("%s\t%d" % (current_license, len(a)))
a.clear()
