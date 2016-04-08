#!/usr/bin/python
import sys
current = None
trip = False
fare = False
trips = []
fares = []
for line in sys.stdin:
    
    key, values = line.strip().split('\t', 1)
    tag, value = values.strip().split('&', 1)
  
    if key != current:    
        if trip and fare:
            for a in trips:
                for b in fares:
                    print "%s\t%s" % (current, a + ',' + b)
            trip = False
            fare = False
            del trips[:]
            del fares[:]

    if tag == '0':
        trips.append(value)
        trip = True   
    if tag == '1':
        fares.append(value)
        fare = True
    current = key
for a in trips:
    for b in fares:
        print "%s\t%s" %(current, a + ',' + b)
    
    
