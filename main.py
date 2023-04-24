import csv
import datetime
import sys
import math
import load_packages
import delivery_truck
import graph
import csv_reader
import HashTable

#print(myhash.search(2))

#print(graph.minimum_distance(load_packages.trucktwo, graph.address_list, graph.distance_list, csv_reader.myhash))

t1_delivery = graph.truckDeliverPackages(load_packages.truckone, graph.address_list, graph.distance_list, load_packages.myhash)
t2_delivery = graph.truckDeliverPackages(load_packages.trucktwo, graph.address_list, graph.distance_list, load_packages.myhash)
t3_delivery = graph.truckDeliverPackages(load_packages.truckthree, graph.address_list, graph.distance_list, load_packages.myhash)



'''
print("-------------------------------------------------------")
print("                      WGUPS                            ")
print("Here at WGUPS we offer a variety of ways to see package delivery metrics.")
print("The total milage for all deliveries is:", t1_delivery[1] + t2_delivery[1] + t3_delivery[1], "miles")

option_input = input("Enter 1 for options.")
if option_input == "1":
    menu_selection = input("Enter m for the total milage of all deliveries.\nEnter t for time menu.\nEnter p for package menu.")
    if menu_selection == "m":
        print("The total milage for all deliveries is:" , t1_delivery[1] + t2_delivery[1] + t3_delivery[1], "miles")
    if menu_selection == "t":
        time_input = input("To print the times of all delivered packages, enter 'a'. To get the times of a single package " \
                     "enter the ID of the package.")
        if time_input == "a":
            print("x") '''


