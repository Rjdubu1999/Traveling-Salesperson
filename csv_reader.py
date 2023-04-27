import csv
import datetime

from Package import Package
from HashTable import Hashtable
from delivery_truck import DeliveryTruck

with open('File_Csv/c950_package.csv') as csv_packages:  # Opening and reading package csv file.
    reader = csv.reader(csv_packages)
    package_list = list(csv_packages)

with open("File_Csv/c950_address.csv") as address_file:  # Opening and reading address csv file.
    address_csv = csv.reader(address_file)

with open('File_Csv/c950_distances.csv') as distance_file:  # Opening and reading distance csv file.
    distance_csv = csv.reader(distance_file)
    distance_data = list(distance_csv)


def load_package_data(packageFile, hashTable):  # Loading package data into the Hashtable
    with open(packageFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:  # Iterates over each package in the CSV package file then creates a package object.
            PACKAGE = Package()
            PACKAGE.package_ID = int(str.strip(row[0]))
            PACKAGE.package_address = row[1]
            PACKAGE.package_city = row[2]
            PACKAGE.package_state = row[3]
            PACKAGE.package_zipcode = row[4]
            PACKAGE.package_deadline = row[5]
            PACKAGE.package_delivery_status = "AT HUB"
            PACKAGE.delivery_time = None
            PACKAGE.load_time = None
            hashTable.insert(PACKAGE.package_ID, PACKAGE)  # Using hashtable insert function to put all package
    return hashTable                                        # and their associated values into hashtable


myhash = Hashtable()  # Initializing hash table
mypackage = myhash.search(1)  # Test of hashtable to see package information is returning
load_package_data('File_Csv/c950_package.csv', myhash)

