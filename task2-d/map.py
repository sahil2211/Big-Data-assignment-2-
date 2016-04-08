#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:

    key, value = line.strip().split('\t')
    pickup_datetime = key.split(',')[3]
    values = value.split(',')
    if len(values) == 17:
	    fare_amount = float(values[11])
	    surcharge = float(values[12])
	    tip_amount = float(values[14])
	    total = fare_amount + surcharge + tip_amount
	    tolls_amount = float(values[15])

    pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

    print ("%s\t%.2f&%.2f" % (pickup_date, total, tolls_amount))
