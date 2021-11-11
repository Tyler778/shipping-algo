import csv
from hash import ChainingHashTable
from Package import Package
from Trucks import truck
import datetime

cht = ChainingHashTable()

truckPkgs = []

truckSpeed = 18
startTime = datetime.datetime(100, 1, 1, 8, 0, 0)
reloadTime = None

def deliveryTime(miles, reloadUse):
    global reloadTime
    global startTime
    if reloadUse == True:
        startTime = reloadTime
    f = (miles/truckSpeed)
    h = int(f)
    m = int((f - h) * 60)
    s = int((((f - h) * 60) - m) * 60)
    add = datetime.timedelta(hours=h, minutes=m, seconds=s)
    current = startTime + add
    return current

def distanceReader():
    with open("DistanceTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        data_read.pop(0)
    return data_read

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

def packageReader():
    with open("PackageTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
    x = 1
    while x < 41:
        sliced = data_read[x][0:7]
        pkg = Package(sliced[0],sliced[1],sliced[2],sliced[3],sliced[4],sliced[5],sliced[6])
        cht.insert(pkg.getId(), pkg)
        if int(pkg.getId()) % 5 == 4:
            truckPkgs.append(pkg)
        x += 1

def distanceBetween(address1, address2):
    index1 = addressList.index(address1)
    index2 = addressList.index(address2)

    return distanceLookup(index1, index2)

def distanceLookup(index1, index2):
    try:
        distance = distanceList[index1][index2]
    except Exception as e:
        distance = distanceList[index2][index1]
    return distance

def minDistanceFrom(fromAddress, truckPackages):
    holdDistance = 100
    nearestAddress = None
    pID = None
    for i in truckPackages:
        tempDistance = float(distanceBetween(fromAddress, i.getAddress()))
        if tempDistance < holdDistance:
            holdDistance = tempDistance
            nearestAddress = i.getAddress()
            pID = i.getId()


    return nearestAddress, pID

def truckLoadPackages():
    #leftover packages not on t2 or t3
    #4 and 40 same spot
    #2 and 33 same spot
    #7 and 29 same spot
    #27 and 35 same spot
    #1, 29, 40    ---  10:30AM
    #5, 10, 11, 12, 17, 23, 24 possible easy moves
    t1 = [1, 2, 4, 7, 27, 29, 33, 35, 40]
    #must be on t2 OR delivered to same spot
    #3 18 36 38 MUST be t2
    #13 14 15 16 19 20 MUST be on same truck
    #39 same spot 13
    #37 same spot 38
    #34 same spot 15, 16
    #21 same spot 2
    #30 AND 8 nearby other delivery locations
    #15    ---  9:00AM
    #37, 13, 14, 16, 20, 34, 30   ---  10:30AM
    #30, 8possible easy moves
    t2 = [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 39, 37, 34, 21, 30, 8]

    #all delayed until 9:05 OR delivered to same spot
    #26 delivered to same spot
    #31 delivered to same spot
    #22 nearby delivery
    #6, 25, 31  --- 10:30AM
    #9 new location is 410 S State St old location is 300 State St
    t3 = [6, 25, 26, 28, 31, 32, 9, 22, 5, 10, 11, 12, 17, 23, 24]

    for i in t1:
        truckOne.load(cht.search(str(i)))
    for i in t2:
        truckTwo.load(cht.search(str(i)))
    for i in t3:
        truckThree.load(cht.search(str(i)))
    return len(t1), len(t2), len(t3)

def truckDeliverPackages(truck, leaveOut, newStart):
    global reloadTime
    hubAddress = addressList[0]
    prevAddress = hubAddress
    remPackages = truck.getAllPackages()
    sum = 0.0
    while truck.getCountOfPackages() > 0:
        addressID = minDistanceFrom(prevAddress, remPackages)
        address = addressID[0]
        id = addressID[1]
        remPackages.remove(cht.search(id))

        truck.removePackageCount()

        sum = float(distanceBetween(prevAddress, address)) + sum
        truck.setMilesTraveled(sum)
        prevAddress = address
        rounded = round(sum, 1)
        tenTwenty = datetime.datetime(100, 1, 1, 10, 19, 59, 0)
        if deliveryTime(sum, newStart).time() >= tenTwenty.time() and cht.search('9').getAddress() == '300 State St':
            cht.search('9').setAddress('410 S State St')
            print('It is past 10:20 and package 9 is now updated.')
        print('Delivery Time: ' + str(deliveryTime(sum, newStart).time()))
        print('Delivered ' + id + ' to ' + address)
        print('I have traveled: ' + str(rounded) + ' miles now!\n')


        if (leaveOut == True) and truck.getCountOfPackages() == 0:
            print('That was my final package and I am staying out.')
            print('I have traveled ' + str(round(truck.getMilesTraveled(), 1)) + ' miles.')
            print('\n')
        elif (leaveOut != True) and truck.getCountOfPackages() == 0:
            homeDist = distanceBetween(prevAddress, hubAddress)
            truck.setMilesTraveled(float(homeDist) + sum)
            reloadTime = deliveryTime(truck.getMilesTraveled(), newStart)
            print("I've returned to the hub to pickup more packages.")
            print('After returning to the hub I have traveled ' + str(round(truck.getMilesTraveled(), 1)) + ' miles and the time is currently ' + str(reloadTime.time()) + '.')
            print('\n')



def grabTotalMileage():
    sum1 = round(truckOne.getMilesTraveled(), 1)
    sum2 = round(truckTwo.getMilesTraveled(), 1)
    sum3 = round(truckThree.getMilesTraveled(), 1)
    total = sum1 + sum2 + sum3
    print('Truck 1 traveled ' + str(sum1) + ' miles and delivered 9 packages.')
    print('Truck 2 traveled ' + str(sum2) + ' miles and delivered 16 packages.')
    print('Truck 3 traveled ' + str(sum3) + ' miles and delivered 15 packages.')
    print('Total mileage driven was ' + str(total) + ' miles.')


addressList = addressReader()
distanceList = distanceReader()
truckOne = truck()
truckTwo = truck()
truckThree = truck()
if __name__ == '__main__':
    print('\n')
    packageReader()
    addressReader()
    truckLoadPackages()
    truckDeliverPackages(truckOne, False, False)
    truckDeliverPackages(truckTwo, True, False)
    truckDeliverPackages(truckThree, True, True)

    grabTotalMileage()
    #ValueError: '5383 South 900 East #104' is not in list
    #print(addressList)