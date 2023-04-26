from datetime import datetime
import delivery_truck
from delivery_truck import DeliveryTruck
from csv_reader import csv_packages
from csv_reader import address_csv
from csv_reader import distance_csv
import csv
from HashTable import Hashtable
from Package import Package
from csv_reader import load_package_data
from csv_reader import myhash
from delivery_truck import DeliveryTruck

# create array to hold package id's

t1 = [2, 21, 10, 22, 17, 23, 40, 24, 39, 26, 35, 29, 30, 27]
t2 = [8, 3, 4, 36, 5, 38, 12, 18, 11, 16, 20, 15, 13, 14, 19]
t3 = [37, 1, 34, 9, 33, 25, 7, 28, 6, 31, 32]
TODAY = datetime.now()

print(TODAY)
#start truck one
START = datetime(TODAY.year, TODAY.month, TODAY.day, 8, 0, 0, 0)
START_two = datetime(TODAY.year, TODAY.month, TODAY.day, 9, 0, 0, 0)
START_three = datetime(TODAY.year, TODAY.month, TODAY.day, 10, 30, 0, 0)
truckone = delivery_truck.DeliveryTruck(16, .3, t1, "4001 South 700 East", 0.0, START, START)
for i in t1:
    myhash.search(i).load_time = START
    myhash.search(i).package_delivery_status = "TRANSIT"
trucktwo = delivery_truck.DeliveryTruck(16, .3, t2, "4001 South 700 East", 0.0, START_two, START_two)
for i in t2:
    myhash.search(i).load_time = START_two
    myhash.search(i).package_delivery_status = "TRANSIT"
truckthree = delivery_truck.DeliveryTruck(16, .3, t3, "4001 South 700 East", 0.0, START_three, START_three)
for i in t3:
    myhash.search(i).load_time = START_three
    myhash.search(i).package_delivery_status = "TRANSIT"
