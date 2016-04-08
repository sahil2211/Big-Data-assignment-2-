#!/usr/bin/python
import sys

for line in sys.stdin:

    key, value = line.strip().split('\t')
    fare_amount = value.split(',')[11]
    fare_amount = float(fare_amount)
    if fare_amount < 0:
        continue
    if fare_amount >= 0 and fare_amount <= 4:
        fare_amount = '0,4'
    elif fare_amount >= 4.01 and fare_amount <= 8:
        fare_amount = '4.01,8'
    elif fare_amount >= 8.01 and fare_amount <= 12:
        fare_amount = '8.01,12'
    elif fare_amount >= 12.01 and fare_amount <= 16:
        fare_amount = '12.01,16'
    elif fare_amount >= 16.01 and fare_amount <= 20:
        fare_amount = '16.01,20'
    elif fare_amount >= 20.01 and fare_amount <= 24:
        fare_amount = '20.01,24'
    elif fare_amount >= 24.01 and fare_amount <= 28:
        fare_amount = '24.01,28'
    elif fare_amount >= 28.01 and fare_amount <= 32:
        fare_amount = '28.01,32'
    elif fare_amount >= 32.01 and fare_amount <= 36:
        fare_amount = '32.01,36'
    elif fare_amount >= 36.01 and fare_amount <= 40:
        fare_amount = '36.01,40'
    elif fare_amount >= 40.01 and fare_amount <= 44:
        fare_amount = '40.01,44'
    elif fare_amount >= 44.01 and fare_amount <= 48:
        fare_amount = '44.01,48'
    elif fare_amount > 48:
        fare_amount = '48.01,infinite'
    print ("%s\t%d" % (fare_amount, 1))
    
    
