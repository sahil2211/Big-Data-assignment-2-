#!/usr/bin/python
import sys

for line in sys.stdin:

    key, value = line.strip().split('\t')

    medallion = key.split(',')[0]
    license = key.split(',')[1]

    print ("%s\t%s" % (license, medallion))
