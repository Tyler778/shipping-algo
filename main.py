#       Tyler Steven Quante
#       Student ID: #001041325
#       DSAII Nearest Neighbor Algorithm
#       Time Complexity of O(n^2)
#       Space Complexity of O(n)
#
import csv
from hash import HashTable
from Package import Package
from Trucks import truck
import datetime
import time

# function deliveryTime() accepts two parameters that take the sum of miles traveled and a boolean as reloadUse
# With this information we can calculate the hours, minutes, and seconds based on the truck speed.  Depending on
# if reloadUse was True or False, we use either 8:00AM or the reloadTime then increment it by the time spent traveling
# miles passed to the function.
#
# O(1) time complexity
# O(1) space complexity
def deliveryTime(miles, reloadUse):
    global reloadTime
    global startTime
    truckSpeed = 18
    if reloadUse == True:
        startTime = reloadTime
    f = (miles/truckSpeed)
    h = int(f)
    m = int((f - h) * 60)
    s = int((((f - h) * 60) - m) * 60)
    add = datetime.timedelta(hours=h, minutes=m, seconds=s)
    current = startTime + add
    return current


# Read through the DistanceTable.csv, format it, and return the data.
#
# O(n) time complexity
# O(n) space complexity
def distanceReader():
    with open("DistanceTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        data_read.pop(0)
    return data_read

# Read through the AddressTable.csv, format it, and input it into the addressList[]
#
# O(n) time complexity
# O(n) space complexity
def addressReader():
    with open("AddressTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        data_read.pop(0)
        listHold = []
        for i in data_read:
            listHold.append(i)
        addressList = [i[0] for i in listHold]
    return addressList

# Read through the PackageTable.csv, slice it, create an instance of the Package class and insert
# it into the Hash Table
#
# O(n) time complexity
# O(n) space complexity
def packageReader():
    with open("PackageTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
    x = 1
    while len(data_read) > x:
        sliced = data_read[x][0:7]
        pkg = Package(sliced[0],sliced[1],sliced[2],sliced[3],sliced[4],sliced[5],sliced[6])
        cht.insert(pkg.getId(), pkg)
        x += 1

# Given two addresses, find the indices of them in the addressList and then return a call to distanceLookup
#
# O(1) time complexity
# O(1) space complexity
def distanceBetween(address1, address2):
    index1 = addressList.index(address1)
    index2 = addressList.index(address2)

    return distanceLookup(index1, index2)

# Given two indices generated in distanceBetween(), access the distanceList[][] and attempt to access the
# available saved distance at the indices.
#
# O(1) time complexity
# O(1) space complexity
def distanceLookup(index1, index2):
    try:
        distance = distanceList[index1][index2]
    except Exception as e:
        distance = distanceList[index2][index1]
    return distance

# Given an address and a list of packages, return the nearestAddress and package ID of the nearest address
# by looping through package list and calling distanceBetween on each package in the list compared to the
# address used to call the function.
#
# O(n) time complexity
# O(n) space complexity
def minDistanceFrom(fromAddress, truckPackages):
    holdDistance = 100
    for i in truckPackages:
        tempDistance = float(distanceBetween(fromAddress, i.getAddress()))
        if tempDistance < holdDistance:
            holdDistance = tempDistance
            nearestAddress = i.getAddress()
            pID = i.getId()


    return nearestAddress, pID


# Accepts no arguments, truckLoadPackages() is to be called once to mount each package in the corresponding
# list to the truck by looping through the list, searching the hash table for the package, and calling a method
# load() in truck to add that package to the truck.
#
# O(n) time complexity
# O(n) space complexity
def truckLoadPackages():
    t1 = [1, 2, 4, 7, 27, 29, 33, 35, 40]
    t2 = [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 39, 37, 34, 21, 30, 8]
    t3 = [6, 25, 26, 28, 31, 32, 9, 22, 5, 10, 11, 12, 17, 23, 24]
    for i in t1:
        pkg = cht.search(str(i))
        truckOne.load(pkg)
        pkg.setEnRoute()
        time.sleep(.05)
        print('Truck 1 Loaded with ' + pkg.getId())
    for i in t2:
        pkg = cht.search(str(i))
        truckTwo.load(pkg)
        pkg.setEnRoute()
        time.sleep(.05)
        print('Truck 2 Loaded with ' + pkg.getId())
    for i in t3:
        pkg = cht.search(str(i))
        truckThree.load(pkg)
        pkg.setEnRoute()
        time.sleep(.05)
        print('Truck 3 Loaded with ' + pkg.getId())
    time.sleep(1)
    print('All trucks loaded..')
    return len(t1), len(t2), len(t3)

#       ----Nearest Known Neighbor Greedy Algorithm----
#
# With arguments as truck object, leaveOut boolean, and newStart Boolean, we go through each package
# within the truck, deliver it, update the package as delivered with time, and increment the sum of mileage
#
# O(n^2) time complexity
# O(n) space complexity
def truckDeliverPackages(truck, leaveOut, newStart):
    global reloadTime
    hubAddress = addressList[0]
    prevAddress = hubAddress
    remPackages = truck.getAllPackages()
    sum = 0.0
    tenTwenty = datetime.datetime(100, 1, 1, 10, 19, 59, 0)
    while truck.getCountOfPackages() > 0:
        # function called minDistanceFrom to give address and package ID
        # O(n) time complexity
        addressID = minDistanceFrom(prevAddress, remPackages)
        address = addressID[0]
        id = addressID[1]

        # hash table lookup function called to obtain package object of correlating ID and remove it
        # from list of available packages and set it delivered
        # O(1) time complexity
        pkg = cht.search(id)
        remPackages.remove(pkg)
        pkg.setDelivered()

        # decrement truck package count for iteration through while loop
        truck.removePackageCount()

        # increment sum with distanceBetween the prevAddress and the new address traveled to
        # set the truck miles traveled with sum
        # prevAddress now points to the new address(after calculating the distance between)
        # set the package delivery time
        sum = float(distanceBetween(prevAddress, address)) + sum
        truck.setMilesTraveled(sum)
        prevAddress = address
        pkg.setDeliveredTime(deliveryTime(sum, newStart).time())

        # check if the delivery time is greater than 10:20 and update the package 9 with correct info
        if deliveryTime(sum, newStart).time() >= tenTwenty.time() and cht.search('9').getAddress() == '300 State St':
            cht.search('9').setAddress('410 S State St')
            cht.search('9').setZip('84111')
        # check if truckDeliverPackages was called with leaveOut as True and if so don't return to the hub
        # otherwise return to the hub and set the reload time as the time you return
        if (leaveOut != True) and truck.getCountOfPackages() == 0:
            homeDist = distanceBetween(prevAddress, hubAddress)
            truck.setMilesTraveled(float(homeDist) + sum)
            reloadTime = deliveryTime(truck.getMilesTraveled(), newStart)

# Rounding of the truck sums and printing the sum for each
#
# O(1) time complexity
# O(1) space complexity
def grabTotalMileage():
    sum1 = round(truckOne.getMilesTraveled(), 1)
    sum2 = round(truckTwo.getMilesTraveled(), 1)
    sum3 = round(truckThree.getMilesTraveled(), 1)
    total = sum1 + sum2 + sum3
    print('Truck 1 traveled ' + str(sum1) + ' miles and delivered 9 packages.')
    time.sleep(.5)
    print('Truck 2 traveled ' + str(sum2) + ' miles and delivered 16 packages.')
    time.sleep(.5)
    print('Truck 3 traveled ' + str(sum3) + ' miles and delivered 15 packages.')
    time.sleep(.5)
    print('Total mileage driven was ' + str(total) + ' miles.')
    time.sleep(4)

# Concise function to deliver all trucks and print such
#
# O(n^2) time complexity
# O(n) space complexity
def deliver():
    try:
        truckDeliverPackages(truckOne, False, False)
        truckDeliverPackages(truckTwo, True, False)
        truckDeliverPackages(truckThree, True, True)
        time.sleep(1)
        print('Successfully delivered packages.')
    except Exception as e:
        print(e)
        print('There was a problem in delivery.')

# Function that takes a time input as a string and queries all packages at that time to see information
#
# O(n) time complexity
# O(n) space complexity
def displayByTime(timeString):
    fixed_time = datetime.datetime.strptime(timeString, '%I:%M:%S').time()
    tenTwenty = datetime.datetime(100, 1, 1, 10, 19, 59, 0).time()
    if fixed_time > tenTwenty:
        cht.search('9').setAddress('410 S State St')
        cht.search('9').setZip('84111')
    else:
        cht.search('9').setAddress('300 State St')
        cht.search('9').setZip('84103')


    print('ID-------Address-------------------------------City---------------------------------------Zip---------Required-------------------------Weight------------------------------------------Status-------------------')
    for i in Package._registry:
        status = 'Not Delivered Yet'

        if fixed_time > i.getDeliveredTime():
            status = 'Delivered at ' + str(i.getDeliveredTime())


        print((str(i.getId()) + '    ' + str(i.getAddress()) + '\t' + str(i.getCity()) + '\t' + str(i.getZip()) + '       ' + str(i.getDeliveryTime()) + '\t' + str(i.getWeight()) + '\t' + status).expandtabs(45))
        print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #line = str(i.getId()) + '\t' + str(i.getAddress()) + '\t' + str(i.getCity()) + '\t' + str(i.getZip()) + '\t' + str(i.getDeliveryTime()) + '\t' + str(i.getWeight())

        #print(line)


# Function to display specific package information based upon the id passed to it.
#
# O(1) time complexity
# O(1) space complexity
def lookupPackage(id):
    pkg = cht.search(id)
    print('Searching...')
    time.sleep(1)
    print('ID-------Address-------------------------------City---------------------------------------Zip-------Required---------------------------Weight------------------------------------------Status-------------------')
    print(((str(pkg.getId()) + '      ' + str(pkg.getAddress()) + '\t' + str(pkg.getCity()) + '\t' + str(pkg.getZip()) + '      ' + str(pkg.getDeliveryTime()) + '\t' + str(pkg.getWeight()) + '\t' + str(pkg.getStatus()))).expandtabs(45))
    time.sleep(3)

#Initializing a few lists, relevant truck objects, hashtable instance, and time values that need to be global.
#
# time and space complexity of O(n)
addressList = addressReader()
distanceList = distanceReader()
truckOne = truck()
truckTwo = truck()
truckThree = truck()
cht = HashTable()
startTime = datetime.datetime(100, 1, 1, 8, 0, 0)
reloadTime = None

# Main function to operate program
#
# Whole program operates at O(n^2) with space complexity of O(n^2)
if __name__ == '__main__':
    # Startup the reader to input package data into the hashtable
    packageReader()


    # Loop user input for menu items and function calls.
    isExit = True
    while (isExit):
        time.sleep(1)
        print("\nOptions:")
        print("1. Load Truck With Packages")
        print("2. Deliver Packages")
        print('3. Total Mileage Info')
        print('4. Time Search')
        print('5. Package Lookup')
        print('6. Close')
        option = input("Option 1 must be done before 2.  3, 4, and 5 can then be done.  6 to close program: ")
        if option == "1":
            truckLoadPackages()
        elif option == "2":
            deliver()
        elif option == "3":
            grabTotalMileage()
        elif option == "4":
            t = input("Type any time to view list of package data at that time.  (Example: 9:30:00)")
            displayByTime(str(t))
        elif option == '5':
            t = input("Type any ID to see detailed information about that package. (Example: 7)")
            lookupPackage(str(t))
        elif option == "6":
            isExit = False
        else:
            print("Wrong option, please try again!")

