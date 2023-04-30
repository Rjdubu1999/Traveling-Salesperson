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
# 1 6 13 14 15 16 20 25 29 30 31 34 37 40
# create array to hold package id's for each individual truck
# assorted packages according to requirements

t1 = [27, 35, 13, 14, 15, 16, 19, 20, 21, 39, 4, 40, 7, 29, 11, 22]
t2 = [3,36,18, 5, 37, 38, 10, 12, 17, 8, 30, 2, 33, 6, 31]
t3 = [32, 28, 9, 23, 24, 26, 1,34,25]
TODAY = datetime.now()

print(TODAY)  # prints today date and time when the program is run
# Start time for each of the delivery trucks
START = datetime(TODAY.year, TODAY.month, TODAY.day, 8, 0, 0, 0)  # start time for first truck
START_two = datetime(TODAY.year, TODAY.month, TODAY.day, 8, 0, 0, 0)  # start time for second truck
START_three = datetime(TODAY.year, TODAY.month, TODAY.day, 9, 45, 0, 0)  # start time for third truck
truckone = delivery_truck.DeliveryTruck(16, .3, t1, "4001 South 700 East", 0.0, START, START)  # initializing truck object
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
