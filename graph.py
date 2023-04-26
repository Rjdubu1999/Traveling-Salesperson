import csv
from datetime import datetime, timedelta
from load_packages import trucktwo
from load_packages import truckthree
import delivery_truck
from load_packages import truckone
from load_packages import alltrucks
from delivery_truck import DeliveryTruck
from csv_reader import myhash
from load_packages import TODAY
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


def delivery(truck, listAddresses, list2DDistances, hTable):
    flag = True
    totalDistance = 0.0
    delivered_packages = [] # initialize list to store delivered packages
    while flag:
        x = minimum_distance(truck, listAddresses, list2DDistances, hTable)
        if x == None:
            flag = False
            break
        else:
            x.package_delivery_status = 'DELIVERED'
            x.delivery_time = truck.current_time # set delivery time to current time
            delivered_packages.append((x.package_ID, x.package_delivery_status, x.delivery_time)) # add package ID, delivery status, and delivery time to list
            dist = distanceBetween(truck.current_location, x.package_address, listAddresses, list2DDistances)
            truck.current_time += timedelta(minutes = float(float(dist)/float(truck.speed)))
            totalDistance += float(dist)
            truck.current_location = x.package_address
            hTable.update(x.package_ID, x)
    disToHub = distanceBetween(truck.current_location, listAddresses[0], listAddresses, list2DDistances)
    truck.current_time += timedelta(minutes = float(float(disToHub)/float(truck.speed)))
    return [disToHub, totalDistance, truck.current_time, delivered_packages] # add delivered_packages list to returned values

#print(delivery(truckone, address_list, distance_list, myhash)[3])

'''
delivery(truckone, address_list, distance_list, myhash)
delivery(trucktwo, address_list, distance_list, myhash)
delivery(truckthree, address_list, distance_list, myhash)
'''

def packageStatusAtTime(givenTime, hTab, numberOfPackages):
    all_deliveries()
    for i in range(1, numberOfPackages + 1):
            pck = hTab.search(i)
            #print(pck)

            if pck.load_time > givenTime:

                print("Package %d is still at the HUB" % i)

            elif givenTime >= pck.load_time and givenTime < pck.delivery_time:

                print("Package %d is ENROUTE ; ETA = %s" % (i, pck.delivery_time))

            elif timeInput >= pck.delivery_time:
                print("Package %d was DELIVERED at %s" % (i, pck.delivery_time))
    return




def all_delivery_t1():
    deliveries_t1 = delivery(truckone, address_list, distance_list, myhash)
    delivered_packages = deliveries_t1[3]
    print("Package delivery times for truck one:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


def all_delivery_t2():
    deliveries_t2= delivery(trucktwo, address_list, distance_list, myhash)
    delivered_packages = deliveries_t2[3]
    print("Package delivery times for truck 2:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


def all_delivery_t3():
    deliveries_t3 = delivery(truckthree, address_list, distance_list, myhash)
    delivered_packages = deliveries_t3[3]
    print("Package delivery times for truck 3:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return
#all_delivery_t3()

def all_deliveries():
    all_delivery_t1()
    all_delivery_t2()
    all_delivery_t3()

#all_deliveries()


def time_input_package():
    time_input = input("Enter time: HH:MM:SS")
    (h,m,s) = time_input.split(":")
    time_convert = timedelta(hours=int(h), minutes=int(m), seconds=int(s))


def delivery_by_id():
    solo = input("Enter ID: ")
    d1 = delivery(truckone, address_list, distance_list, myhash)
    d2 = delivery(trucktwo, address_list, distance_list, myhash)
    d3 = delivery(truckthree, address_list, distance_list, myhash)
    delivered_packages = d1[3] + d2[3] + d3[3]
    for package in delivered_packages:
        if package[0] == int(solo):
            delivery_time = package[2]
            print(f"Package ID {solo} delivered at {delivery_time}.")
            return
    print(f"Package ID {solo} not found.")


def delivery_by_time():
    time_input = input("Enter time in format HH:MM:SS to see status of packages at specific time. ")
    (h,m,s) = time_input.split(":")
    convert_time = datetime(TODAY.year, TODAY.month, TODAY.day, int(h), int(m), int(s))
    d1 = delivery(truckone, address_list, distance_list, myhash)
    d2 = delivery(trucktwo, address_list, distance_list, myhash)
    d3 = delivery(truckthree, address_list, distance_list, myhash)
    all_d = d1, d2, d3
    for delivery_data in all_d:
        delivered_packages = delivery_data[3]  # get the delivered packages from the delivery data
        print(f"Delivery status at {convert_time}:")
        for package in delivered_packages:
            if package[2] <= convert_time:  # check if package was delivered before or at the specified time
                print(f"Package ID: {package[0]}, Delivery status: {package[1]}")



#delivery_by_time()




while True:
    print('\nWelcome to WGUPS!')
    print('Please choose an option:')
    print('1. Print total mileage')
    print('2. Print delivery time of a single package')
    print('3. Print delivery times of all packages')
    print('4. Enter a time to find all packages status')
    print('5. Exit program')
    choice = input('> ')

    if choice == '1':
        deliveryInfo1 = delivery(truckone, address_list, distance_list, myhash)
        deliveryInfo2 = delivery(trucktwo, address_list, distance_list, myhash)
        deliveryInfo3 = delivery(truckthree, address_list, distance_list, myhash)
        total_mileage = deliveryInfo1[1] + deliveryInfo2[1] + deliveryInfo3[1]
        print(f'Total mileage: {total_mileage} miles')
        break
    elif choice == '2':
        delivery_by_id()
        break
    elif choice == '3':
        all_deliveries()
        break
    elif choice == '4':
        hour = input("Enter Hour as an Integer 0-23: ")

        hour = int(str.strip(hour))

        print(hour)

        minute = input("Enter Minute as an Integer 0 - 59: ")

        minute = int(str.strip(minute))

        print(minute)

        timeInput = datetime(TODAY.year, TODAY.month, TODAY.day, hour, minute, 0, 0)

        print(type(timeInput))
        packageStatusAtTime(timeInput, myhash, 40)

        break
    elif choice == '5':
        print('Exiting program...')
        break

    else:
        print('Invalid choice. Please try again.')

#for i in range(1,41):
#   print(myhash.search(i))


