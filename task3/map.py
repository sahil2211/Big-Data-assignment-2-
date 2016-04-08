#!/usr/bin/python
import sys
import csv
import StringIO

 
for line in sys.stdin:
    if '\t' in line:
        key, value = line.strip().split('\t')
        
        

        keys = key.split(',')
        values = value.split(',')

        medallion, hack_license, vendor_id, pickup_datetime = keys
        rate_code = values[0]
        store_and_fwd_flag = values[1] 
        dropoff_datetime = values[2] 
        passenger_count = values[3] 
        trip_time_in_secs = values[4] 
        trip_distance = values[5] 
        pickup_longitude = values[6] 
        pickup_latitude = values[7] 
        dropoff_longitude = values[8] 
        dropoff_latitude = values[9] 
        payment_type = values[10] 
        fare_amount = values[11] 
        surcharge = values[12] 
        mta_tax = values[13] 
        tip_amount = values[14] 
        tolls_amount = values[15] 
        total_amount = values[16] 

        print ('%s\t0|%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, vendor_id, pickup_datetime, rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount))

    else:
        csv_file = StringIO.StringIO(line)
        csv_reader = csv.reader(csv_file)
        for values in csv_reader:
            license = []
            for v in values:
                if ',' in v:
                    license.append('"' + v + '"')
                else:
                    license.append(v)
            medallion = license[0] 
            name = license[1] 
            type = license[2] 
            current_status = license[3] 
            DMV_license_plate = license[4] 
            vehicle_VIN_number = license[5] 
            vehicle_type = license[6] 
            model_year = license[7] 
            medallion_type = license[8] 
            agent_number = license[9] 
            agent_name = license[10] 
            agent_telephone_number = license[11] 
            agent_website = license[12] 
            agent_address = license[13] 
            last_updated_date = license[14] 
            last_updated_time = license[15] 

            if medallion != "medallion":
                print ('%s\t1|%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (medallion, name, type, current_status, DMV_license_plate, vehicle_VIN_number, vehicle_type, model_year, medallion_type, agent_number, agent_name, agent_telephone_number, agent_website, agent_address, last_updated_date, last_updated_time))
