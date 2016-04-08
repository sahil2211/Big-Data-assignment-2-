#!/usr/bin/python
import sys
import csv
import StringIO
 
for line in sys.stdin:
    key, value = line.strip().split('\t')
    csv_file = StringIO.StringIO(value)
    csv_reader = csv.reader(csv_file)
    for values in csv_reader:
        
        agent_name = values[29] if len(values) > 29 else ''

        try:
            fare_amount = float(values[14]) if len(values) > 14 else ''
            surcharge = float(values[15]) if len(values) > 15 else ''
            tip_amount = float(values[17]) if len(values) > 17 else ''
           
        except ValueError:
            continue

        revenue = fare_amount + surcharge + tip_amount 

        print ('%s\t%f' % (agent_name, revenue))
