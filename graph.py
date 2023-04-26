import csv
from datetime import datetime, timedelta
from load_packages import trucktwo
from load_packages import truckthree
import delivery_truck
from load_packages import truckone
from delivery_truck import DeliveryTruck
from csv_reader import myhash
from load_packages import TODAY
import Package


def load_address_data(filename):
    address_data = []

    with open(filename) as address_file:
        csv_reader = csv.reader(address_file, delimiter=',')

        for row in csv_reader:
            address_data.append(str.strip(row[2]))

    return address_data


load_address_data('File_Csv/c950_address.csv')

def load_distance_data(filename):
    distance_data = []
    with open(filename) as distance_file:
        reader = csv.reader(distance_file)
        for row in reader:
            distance_data.append(row)
        return distance_data


address_list = load_address_data('File_Csv/c950_address.csv')
distance_list = load_distance_data('File_Csv/c950_distances.csv')


def distance_between(address1, address2, addressList, distanceList):
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


def minimum_distance(truck, list_addresses, list_distances, hTable):
    package_dict = dict()
    truck_packages = [hTable.search(i) for i in truck.packages]
    truckPackages = [x for x in truck_packages if x.package_address != truck.current_location and x.package_delivery_status == 'TRANSIT']
    for pack in truckPackages:
        package_dict[pack.package_ID] = float(
            distance_between(truck.current_location, pack.package_address, list_addresses, list_distances))
    if len(package_dict) > 0:
        return hTable.search(int(min(package_dict.items(), key=lambda x: x[1])[0]))
    else:
        return None


package_distance = minimum_distance(truckone, address_list, distance_list, myhash)


def delivery(truck, listAddresses, list2DDistances, hTable):
    flag = True
    total_distance = 0.0
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
            dist = distance_between(truck.current_location, x.package_address, listAddresses, list2DDistances)
            truck.current_time += timedelta(minutes=float(float(dist)/float(truck.speed)))
            total_distance += float(dist)
            truck.current_location = x.package_address
            hTable.update(x.package_ID, x)
    disToHub = distance_between(truck.current_location, listAddresses[0], listAddresses, list2DDistances)
    truck.current_time += timedelta(minutes=float(float(disToHub)/float(truck.speed)))
    return [disToHub, total_distance, truck.current_time, delivered_packages] # add delivered_packages list to returned values


def all_delivery_for_time_input1():
    deliveries_t1 = delivery(truckone, address_list, distance_list, myhash)
    delivered_packages = deliveries_t1[3]
    return delivered_packages


def all_delivery_for_time_input2():
    deliveries_t1 = delivery(trucktwo, address_list, distance_list, myhash)
    t2 = deliveries_t1[3]
    return t2


def all_delivery_for_time_input3():
    deliveries_t3 = delivery(truckthree, address_list, distance_list, myhash)
    t3 = deliveries_t3[3]
    return t3


def total_input():
    all_delivery_for_time_input1()
    all_delivery_for_time_input2()
    all_delivery_for_time_input3()


def package_time_status(given_time, h_table, packages):
    total_input()
    for i in range(1, packages + 1):
            pck = h_table.search(i)
            if pck.load_time > given_time:
                print("Package %d is still at the HUB" % i)
            elif given_time >= pck.load_time and given_time < pck.delivery_time:
                print("Package %d is ENROUTE. The ETA is %s" % (i, pck.delivery_time))
            elif timeInput >= pck.delivery_time:
                print("Package %d was DELIVERED at %s" % (i, pck.delivery_time))
    return


def all_delivery_t1():
    deliveries_t1 = delivery(truckone, address_list, distance_list, myhash)
    delivered_packages = deliveries_t1[3]
    print("Delivery times for truck one:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


def all_delivery_t2():
    deliveries_t2 = delivery(trucktwo, address_list, distance_list, myhash)
    delivered_packages = deliveries_t2[3]
    print("Delivery times for truck 2:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


def all_delivery_t3():
    deliveries_t3 = delivery(truckthree, address_list, distance_list, myhash)
    delivered_packages = deliveries_t3[3]
    print("Delivery times for truck 3:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


def all_deliveries():
    all_delivery_t1()
    all_delivery_t2()
    all_delivery_t3()


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
        package_time_status(timeInput, myhash, 40)
        break
    elif choice == '5':
        print('Exiting program...')
        break
    else:
        print('Invalid choice. Please try again.')




