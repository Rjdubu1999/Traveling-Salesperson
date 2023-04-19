import datetime

import delivery_truck
from delivery_truck import DeliveryTruck
from csv_reader import csv_packages
from csv_reader import address_csv
from csv_reader import distance_csv
import csv
from HashTable import Hashtable
from Package import Package
from csv_reader import loadPackageData
from csv_reader import myhash
from delivery_truck import DeliveryTruck

# create array to hold package id's

t1 = [2, 21, 10, 22, 17, 23, 40, 24, 39, 26, 35, 29, 30]
t2 = [8, 3, 4, 36, 5, 38, 12, 18, 11, 16, 20, 15, 13, 14, 19]
t3 = [37, 1, 34, 9, 33, 25, 7, 28, 6, 31, 32]
#pkg = myhash.search(1)
#print(pkg)
truckone = delivery_truck.DeliveryTruck(16, 18, t1, "4001 South 700 East", 0.0, datetime.timedelta(hours=8), None, None )
trucktwo = delivery_truck.DeliveryTruck(16, 18, t2, "4001 South 700 East", 0.0, datetime.timedelta(hours=8), None, None )
truckthree = delivery_truck.DeliveryTruck(16, 18, t3, "4001 South 700 East", 0.0, datetime.timedelta(hours=8), None, None )
#print(truckone)
#print(trucktwo)

#print(truckthree)