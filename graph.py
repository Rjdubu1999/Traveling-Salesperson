import csv
from datetime import datetime, timedelta
from load_packages import trucktwo
from load_packages import truckthree
import delivery_truck
from load_packages import truckone
from load_packages import alltrucks
from delivery_truck import DeliveryTruck
from csv_reader import myhash

import Package
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

#print(address_list)


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
#print(a)
addressData = loadAddressData('File_Csv/c950_address.csv')
#addressData2 = loadAddressData('File_Csv/c950_address.csv')

def minimum_distance(truck, listAddresses, list2DDistances, hTable):
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

#print(minimum_distance(truckthree, address_list, distance_list, myhash))


package_distance = minimum_distance(truckone, address_list, distance_list, myhash)


def truckDeliverPackages(truck, listAddresses, list2DDistances, hTable):

    flag = True

    totalDistance = 0.0

    while flag:

        x = minimum_distance(truck, listAddresses, list2DDistances, hTable)

        if x == None:

            flag = False

            break

        else:

            x.package_delivery_status = 'DELIVERED'
            print(x)

            dist = distanceBetween(truck.current_location, x.package_address, listAddresses, list2DDistances)
            #print(truck.current_time)
            #print(truck.speed)
            #print(dist)
            truck.current_time += timedelta(minutes = float(float(dist)/float(truck.speed)))
            print(truck.current_time)
            x.tDel = truck.current_time

            totalDistance += float(dist)

            truck.current_location = x.package_address

            hTable.update(x.package_ID, x)

    disToHub = distanceBetween(truck.current_location, listAddresses[0], listAddresses, list2DDistances)
    #truck.speed = float(truck.speed)
    truck.current_time += timedelta(minutes = float(float(disToHub)/float(truck.speed)))
    print(truck.current_time)
    return [disToHub, totalDistance, truck.current_time]


print(truckDeliverPackages(trucktwo,address_list, distance_list, myhash)[2], "\n")

print(truckDeliverPackages(truckone,address_list, distance_list, myhash)[2], "\n")

print(truckDeliverPackages(truckthree,address_list, distance_list, myhash)[2], "\n")

'''
def package_delivery(truck, address_list, distance_list, htable):
    flag = True
    distance_keeper = 0.0
    while flag:
        var = minimum_distance(truck, address_list, distance_list, htable)
        if var == None:
            flag = False
            break
        else:
            var.delivery_status = 'Delivered'
            distance = distanceBetween(truck.current_location, package_distance, address_list, distance_list )
            print(distance)
            
            truck.current_time += datetime.timedelta(minutes=float(distance/truck.speed))
            var.tDel = truck.current_time
            distance_keeper += distance
            truck.current_location = var.package_address
            htable.update(var.package_id, var)

            distance_to_hub = distanceBetween(truck.current_location,address_list[0], address_list, distance_list)
            truck.current_time += datetime.timedelta(minutes=float(distance_to_hub/truck.speed))
            return[distance_to_hub, distance_keeper, truck.current_time] 


print(package_delivery(truckone, address_list, distance_list, myhash)) '''
'''
'''


