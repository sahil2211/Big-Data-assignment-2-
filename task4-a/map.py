#!/usr/bin/python
import sys
import csv
import StringIO
 
for line in sys.stdin:
    key, value = line.strip().split('\t')
    csv_file = StringIO.StringIO(value)
    csv_reader = csv.reader(csv_file)
    for values in csv_reader:
        
        vehicle_type = values[25] if len(values) > 25 else ''

        try:
            fare_amount = float(values[14]) if len(values) > 14 else ''
            surcharge = float(values[15]) if len(values) > 15 else ''
            
            tip_amount = float(values[17]) if len(values) > 17 else ''
            
            
        except ValueError:
            continue

        revenue = fare_amount + surcharge + tip_amount 

        tip_amount = tip_amount if revenue else 0

        print ('%s\t%f,%f,%d' % (vehicle_type, revenue, tip_amount, 1))
    
