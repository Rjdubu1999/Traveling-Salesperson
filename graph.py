import csv

import delivery_truck
from load_packages import truckone
from delivery_truck import DeliveryTruck
from csv_reader import myhash
'''with open('File_Csv/c950_address.csv') as address_file2:
    reader = csv.reader(address_file2, delimeter=',')
    listAddresses = []
    for row in reader:
        listAddresses.append(str.strip(row[2]))'''

'''with open('File_Csv/c950_distances.csv') as dist_file:
    dist_reader = csv.reader(dist_file, delimeter=',')'''



def loadAddressData(fileName):
    addressData = []

    with open(fileName) as address_file:
        csv_reader = csv.reader(address_file, delimiter=',')

        for row in csv_reader:
            addressData.append(str.strip(row[2]))

    return addressData

loadAddressData('File_Csv/c950_address.csv')

def loadDistanceData(filename):
    distancedata = []
    with open(filename) as distance_file:
        reader = csv.reader(distance_file)
        for row in reader:
            distancedata.append(row)
        return distancedata

address_list = loadAddressData('File_Csv/c950_address.csv')
distance_list = loadDistanceData('File_Csv/c950_distances.csv')

print(address_list)


def distanceBetween(address1, address2, addressList, distanceList):

    if address1 not in addressList or address2 not in addressList:

        print("One or Both Locations is INVALID")

        return

    else:

        i = addressList.index(address1)

        j = addressList.index(address2)

        if i > j:

            return distanceList[i][j]

        else:

            return distanceList[j][i]

a = distanceBetween("1060 Dalton Ave S", "1330 2100 S", address_list, distance_list)
print(a)
#addressData = loadAddressData('File_Csv/c950_address.csv')
#addressData2 = loadAddressData('File_Csv/c950_address.csv')

def minDistFrom2(truck, listAddresses, list2DDistances, hTable):
    dictPackageDistance = dict()
    truck_packages = [hTable.search(i) for i in truck.packages]
    #for p in truck_packages:
        #print(p.package_ID)

    truckPackages = [x for x in truck_packages if x.package_address != truck.current_location and x.package_delivery_status == 'TRANSIT']

    for pack in truckPackages:
        dictPackageDistance[pack.package_ID] = float(
            distanceBetween(truck.current_location, pack.package_address, listAddresses, list2DDistances))


    if len(dictPackageDistance) > 0:

        return hTable.search(int(min(dictPackageDistance.items(), key=lambda x: x[1])[0]))
    
    else:
        return None

print(minDistFrom2(truckone, address_list, distance_list, myhash))

'''
def find_distance(address1, address2):
    with open('File_Csv/c950_distances.csv') as distances:
        reader = csv.reader(distances)
        reader = list(reader)
        dist = reader[address1][address2]
        if dist == '':
            dist = reader[address2][address1]
        return float(dist)

index1 = addressData.index("195 W Oakland Ave")
index2 = addressData.index("233 Canyon Rd")
#print(index2 )
#print(index1)

print(find_distance(index1, index2))


prin_dist = find_distance(addressData.index("195 W Oakland Ave"), addressData.index("233 Canyon Rd"))
#print(prin_dist)
'''


'''
def minDistFrom2(DeliveryTruck, hTable):

    dictPackageDistance = dict()
    packagelist = []
    for i in DeliveryTruck.packages:
        packagelist.append(hTable.search(i))
    for x in packagelist:
        print(x.package_ID)
    truckPackages = [x for x in packagelist if x.package_address != DeliveryTruck.current_location and x.package_delivery_status == 'TRANSIT']

    for pack in truckPackages:
        index = addressData.index(DeliveryTruck.current_location)
        print(index)
        index_two = addressData.index(pack.package_address)
        print(index_two)
        dictPackageDistance[pack.package_ID] = float(find_distance(index, index_two))

    if len(dictPackageDistance) > 0:

        return hTable.search(int(min(dictPackageDistance.items(), key = lambda x : x[1])[0]))

    else:

        return None

a = minDistFrom2(truckone, myhash)
print(a)

'''
