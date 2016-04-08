#!/usr/bin/python
import sys

for line in sys.stdin:
    line0 = line.strip().split(',')
    if line0[0] == 'medallion':
        continue
    if len(line0) == 14:
        medallion = line0[0] 
        hack_license = line0[1] 
    	vendor_id = line0[2] 
    	rate_code = line0[3] 
    	store_and_fwd_flag = line0[4] 
    	pickup_datetime = line0[5] 
    	dropoff_datetime = line0[6] 
    	passenger_count = line0[7] 
    	trip_time_in_secs = line0[8] 
    	trip_distance = line0[9] 
    	pickup_longitude = line0[10] 
    	pickup_latitude = line0[11] 
    	dropoff_longitude = line0[12] 
    	dropoff_latitude = line0[13] 
    	print "%s,%s,%s,%s\t0&%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude)
    if len(line0) == 11:
        medallion = line0[0] 
        hack_license = line0[1] 
        vendor_id = line0[2] 
        pickup_datetime = line0[3] 
        payment_type = line0[4] 
        fare_amount = line0[5] 
        surcharge = line0[6] 
        mta_tax = line0[7] 
        tip_amount = line0[8] 
        tolls_amount = line0[9] 
        total_amount = line0[10] 
        print "%s,%s,%s,%s\t1&%s,%s,%s,%s,%s,%s,%s" % (medallion, hack_license, vendor_id, pickup_datetime, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount)





