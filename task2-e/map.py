#!/usr/bin/python
import sys
from datetime import datetime
for line in sys.stdin:

    key, value = line.strip().split('\t')
    pickup_datetime = key.split(',')[3]
    medallion = key.split(',')[0]
    pickup_date = datetime.strptime(pickup_datetime, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
    print ("%s\t%s,%d" % (medallion,pickup_date,1))
