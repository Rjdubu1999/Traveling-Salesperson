'''
Ryan Wilkinson
Student ID: 001360794
Class: Data Structures and Algorithms II
'''

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


def load_address_data(filename):  # loading address data from csv file
    address_data = []  # empty list to store all addresses
    with open(filename) as address_file:  # opening and reading csv file info
        csv_reader = csv.reader(address_file, delimiter=',')
        for row in csv_reader:   # for loop -> O(n)
            address_data.append(str.strip(row[2]))
    return address_data


load_address_data('File_Csv/c950_address.csv')  # Calling function to get address data

def load_distance_data(filename):  # function to load distance data
    distance_data = []  # empty list to store distance data
    with open(filename) as distance_file: # opening and reading distance csv file
        reader = csv.reader(distance_file)
        for row in reader:  # for loop -> O(n)
            distance_data.append(row)
        return distance_data


address_list = load_address_data('File_Csv/c950_address.csv')  # creating variable to be used in delivery function with address data
distance_list = load_distance_data('File_Csv/c950_distances.csv') # creating variable to be used in delivery function with distance data


# time complexity of distance_between() is O(n) due to the index method
def distance_between(address1, address2, addressList, distanceList):  # function to calculate distance between two points
    if address1 not in addressList or address2 not in addressList:  # finds if an address is address list, if not it prints out an invalid statement
        print("One or Both Locations is INVALID")
        return
    else:
        i = addressList.index(address1)
        j = addressList.index(address2)
        if i > j:
            return distanceList[i][j]  # returns the lesser of two address distances
        else:
            return distanceList[j][i]  # inverts the address values


# time complexity of minimum distance = O(n) * O(log n) = O(n log n)
def minimum_distance(truck, list_addresses, list_distances, hTable):  # function to find the minimum distance from trucks current location
    package_dict = dict()  # create dictionary of packages
    truck_packages = [hTable.search(i) for i in truck.packages]  # searches packages on truck
    truckPackages = [x for x in truck_packages if x.package_address != truck.current_location and x.package_delivery_status == 'TRANSIT']
    for pack in truckPackages:  # find distance from trucks current location to each package address | for = O(n)
        package_dict[pack.package_ID] = float(
            distance_between(truck.current_location, pack.package_address, list_addresses, list_distances))
    if len(package_dict) > 0:
        return hTable.search(int(min(package_dict.items(), key=lambda x: x[1])[0]))  # find package with shortest distance and return package object
                                                                                     # min function = O(logn)
    else:
        return None


package_distance = minimum_distance(truckone, address_list, distance_list, myhash)  # assigning min distance function to variable

# Time complexity of delivery is O(n) * O(n) * O(n log n) = O(n^2 log n)
def delivery(truck, listAddresses, list2DDistances, hTable):  #
    flag = True
    total_distance = 0.0  # setting distance to 0.0 to keep track of milage
    delivered_packages = []  # initialize list to store delivered packages
    while flag:  # loop through all packages | Time complexity: while loop is O(n)
        x = minimum_distance(truck, listAddresses, list2DDistances, hTable)  # locate closest location to trucks location
                                                                             # min dist is O(n log n)
        if x == None:  # exit loops when there are no more packages
            flag = False
            break
        else:  # update package and set delivery status to delivered
            x.package_delivery_status = 'DELIVERED'
            x.delivery_time = truck.current_time  # set delivery time to current time
            delivered_packages.append((x.package_ID, x.package_delivery_status, x.delivery_time)) # add package ID, delivery status, and delivery time to list
            dist = distance_between(truck.current_location, x.package_address, listAddresses, list2DDistances)  # T.C of dist_between is O(n)
            # find distance to package address and update trucks current time
            truck.current_time += timedelta(minutes=float(float(dist)/float(truck.speed)))
            total_distance += float(dist)
            truck.current_location = x.package_address
            hTable.update(x.package_ID, x)  # update package information in hash table
    disToHub = distance_between(truck.current_location, listAddresses[0], listAddresses, list2DDistances)  # find distance back to hub
    truck.current_time += timedelta(minutes=float(float(disToHub)/float(truck.speed)))
    return [disToHub, total_distance, truck.current_time, delivered_packages]  # return the delivery information


def all_delivery_for_time_input1():  # function that gets all the delivery times of delivery truck one to be used for a user input
    deliveries_t1 = delivery(truckone, address_list, distance_list, myhash)  #  O(n^2 log n)
    delivered_packages = deliveries_t1[3]
    return delivered_packages


def all_delivery_for_time_input2():  # # function that gets all the delivery times of delivery truck two to be used for a user input
    deliveries_t1 = delivery(trucktwo, address_list, distance_list, myhash)  #  O(n^2 log n)
    t2 = deliveries_t1[3]
    return t2


def all_delivery_for_time_input3():  # # function that gets all the delivery times of delivery truck three to be used for a user input
    deliveries_t3 = delivery(truckthree, address_list, distance_list, myhash)  # O(n^2 log n)
    t3 = deliveries_t3[3]
    return t3


#  total time complexity is O(n^2 log n) * O(n^2 log n) * O(n^2 log n) = O(n^6 log^3 n)
def total_input():  # function which calls all the other time input delivery functions to combine them
    all_delivery_for_time_input1()  # O (n^2 log n)
    all_delivery_for_time_input2()  # O(n^2 log n)
    all_delivery_for_time_input3()  # O(n^2 log n)


# Function that will give status of all packages based on a given time
def package_time_status(given_time, h_table, packages):  # time complexity: O(n^6 log^3 n) * n = O(N^6 log^3 N)
    total_input()  # calls the total input function
    for i in range(1, packages + 1):  # loops through packages in hash table
            pck = h_table.search(i)  # gets information with search method
            if pck.load_time > given_time:  # check if package is at hub with package load time
                print("Package %d is at the HUB" % i)  # prints the packages status at specific time
            elif given_time >= pck.load_time and given_time < pck.delivery_time:
                print("Package %d is EN ROUTE. The ETA is %s" % (i, pck.delivery_time))
            elif timeInput >= pck.delivery_time:
                print("Package %d was DELIVERED at %s" % (i, pck.delivery_time))
    return


# function that loops through the delivery information of each package id and tells when it was delivered
def all_delivery_t1():  #  Time complexity: O(n log n)
    deliveries_t1 = delivery(truckone, address_list, distance_list, myhash)
    delivered_packages = deliveries_t1[3]
    print("Delivery times for truck one:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


# function that loops through the delivery information of each package id and tells when it was delivered
def all_delivery_t2():  # Time complexity: O(n log n)
    deliveries_t2 = delivery(trucktwo, address_list, distance_list, myhash)
    delivered_packages = deliveries_t2[3]
    print("Delivery times for truck 2:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


# function that loops through the delivery information of each package id and tells when it was delivered
def all_delivery_t3():  # Time complexity: O(n log n)
    deliveries_t3 = delivery(truckthree, address_list, distance_list, myhash)
    delivered_packages = deliveries_t3[3]
    print("Delivery times for truck 3:")
    for package in delivered_packages:
        print(f"Package {package[0]}: {package[1]} at {package[2]}")
    return


# Function which calls the three all_delivery functions to get the times of all functions
def all_deliveries():  # Time complexity is O(n log n) * O(n log n) * O(n log n) = O(n^6 log^3 n )
    all_delivery_t1()
    all_delivery_t2()
    all_delivery_t3()


# function which returns the delivery time of a single package given its ID
# time complexity is O(n log n) * O(n log n) * O(n log n) = O(n^6 log^3 n)
def delivery_by_id():
    id = input("Enter ID: ")  # input for user to enter an ID
    d1 = delivery(truckone, address_list, distance_list, myhash)  # call the delivery function on all 3 trucks
    d2 = delivery(trucktwo, address_list, distance_list, myhash)
    d3 = delivery(truckthree, address_list, distance_list, myhash)
    delivered_packages = d1[3] + d2[3] + d3[3]  # add the three trucks delivery info together
    for package in delivered_packages:  # loops over all delivered packages
        if package[0] == int(id):  # finds if the package id is equal to the input
            delivery_time = package[2]
            print(f"Package ID {id} delivered at {delivery_time}.")  # prints the package id and delivery time
            return
    print(f"Package ID {id} not found.")

#  Command Line interface which gives users 4 options to get data from the sim and 1 to quit program
while True:  # while loop which will allow the user to input vales into the CLI
    print('\nWelcome to WGUPS!')
    print('Please choose an option:')
    print('1. Print total mileage')
    print('2. Print delivery time of a single package')
    print('3. Print delivery times of all packages')
    print('4. Enter a time to find all packages status')
    print('5. Exit program')
    choice = input('> ')

    if choice == '1':  # if user enters 1 it will print the total mileage of the sim
        deliveryInfo1 = delivery(truckone, address_list, distance_list, myhash)
        deliveryInfo2 = delivery(trucktwo, address_list, distance_list, myhash)
        deliveryInfo3 = delivery(truckthree, address_list, distance_list, myhash)
        total_mileage = deliveryInfo1[1] + deliveryInfo2[1] + deliveryInfo3[1]  # adds mileages of all trucks
        print(f'Total mileage: {total_mileage} miles')
        break
    elif choice == '2':  # allows user to input an ID and return the delivery time of package
        delivery_by_id()
        break
    elif choice == '3':  # returns to user all the delivery of times of each truck
        all_deliveries()
        break
    elif choice == '4':  # allows user to enter a time and outputs the status of packages at input time
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
    elif choice == '5':  # quits program
        print('Exiting program...')
        break
    else:
        print('Invalid choice. Please try again.')




