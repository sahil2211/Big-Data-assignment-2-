#!/usr/bin/python
import sys

current_pickup_date = None
current_total = 0
current_tolls_amount = 0

for line in sys.stdin:
    
    pickup_date, revenue = line.strip().split("\t", 1)
    total, tolls_amount = revenue.strip().split("&", 1)
    
    try:
        total = float(total)
        tolls_amount = float(tolls_amount)
    except ValueError:
        continue
    
    if pickup_date == current_pickup_date:
        current_total += total
        current_tolls_amount += tolls_amount
    else:
        if current_pickup_date:
            print ("%s\t%.2f,%.2f" % (current_pickup_date, current_total, current_tolls_amount))
        current_pickup_date = pickup_date
        current_total = total
        current_tolls_amount = tolls_amount

print ("%s\t%.2f,%.2f" % (current_pickup_date, current_total, current_tolls_amount))
