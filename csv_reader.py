import csv
import datetime

from Package import Package
from HashTable import Hashtable
from delivery_truck import DeliveryTruck

with open('File_Csv/c950_package.csv') as csv_packages:
    reader = csv.reader(csv_packages)
    package_list = list(csv_packages)

with open("File_Csv/c950_address.csv") as address_file:
    address_csv = csv.reader(address_file)

with open('File_Csv/c950_distances.csv') as distance_file:
    distance_csv = csv.reader(distance_file)
    distance_data = list(distance_csv)


def loadPackageData(packageFile, hashTable):

    with open(packageFile) as csv_file:

        csv_reader = csv.reader(csv_file, delimiter = ',')

        for row in csv_reader:

            PACKAGE = Package()

            PACKAGE.package_ID = int(str.strip(row[0]))

            PACKAGE.package_address = row[1]
            PACKAGE.package_city = row[2]
            PACKAGE.package_state = row[3]
            PACKAGE.package_zipcode = row[4]
            PACKAGE.package_deadline = row[5]
            PACKAGE.package_delivery_status = 'TRANSIT'
            #PACKAGE.delivery_time = row[6]

            hashTable.insert(PACKAGE.package_ID, PACKAGE)

    return hashTable

myhash = Hashtable()
# using hashtable search to verify that data is loaded into Hash table
mypackage = myhash.search(1)
loadPackageData('File_Csv/c950_package.csv', myhash)

#for i in range(len(myhash.list) +2):
   # print(myhash.search(i+2))


#truck = DeliveryTruck(16, 18, "4100 South 700 East", 0, datetime.timedelta(hours=8), None, None)

#print(truck)
