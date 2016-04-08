#!/usr/bin/python
import sys
current = None
tripfare = False
vehicle = False
tripsfares = []
vehicles = []
for line in sys.stdin:
    
    key, values = line.strip().split('\t', 1)
    tag, value = values.strip().split('|', 1)
  
    if key != current:    
        if tripfare and vehicle:
            for a in tripsfares:
                for b in vehicles:
                    print "%s\t%s" % (current, a + ',' + b)
            tripfare = False
            vehicle = False
            del tripsfares[:]
            del vehicles[:]

    if tag == '0':
        tripsfares.append(value)
        tripfare = True   
    if tag == '1':
        vehicles.append(value)
        vehicle = True
    current = key
for a in tripsfares:
    for b in vehicles:
        print "%s\t%s" %(current, a + ',' + b)
    
del tripsfares[:]
del vehicles[:]
