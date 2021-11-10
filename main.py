import csv
from WGUhash import ChainingHashTable
from Package import Package
from Trucks import truck

cht = ChainingHashTable()

truckPkgs = []

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
    t1 = [1, 2, 4, 5, 7, 10, 11, 12, 17, 23, 24, 27, 29, 33, 35, 40]
    #must be on t2 OR delivered to same spot
    #3 18 36 38 MUST be t2
    #13 14 15 16 19 20 MUST be on same truck
    #39 delivered to same spot 13
    #37 delivered to same spot 38
    #34 delivered to same spot 15, 16
    #21 delivered to same spot as 2
    #30 AND 8 nearby other delivery locations
    #15 9:00AM
    #37, 13, 14, 16, 20, 34   ---  10:30AM
    t2 = [3, 18, 36, 38, 13, 14, 15, 16, 19, 20, 39, 37, 34, 21, 30, 8]

    #all delayed until 9:05 OR delivered to same spot
    #26 delivered to same spot
    #31 delivered to same spot
    #22 nearby delivery
    #6, 25, 31  --- 10:30AM
    t3 = [6, 25, 26, 28, 31, 32, 9, 22]

    for i in t1:
        truckOne.load(cht.search(str(i)))
    for i in t2:
        truckTwo.load(cht.search(str(i)))
    for i in t3:
        truckThree.load(cht.search(str(i)))
    return len(t1), len(t2), len(t3)

def truckDeliverPackages(truck):
    address = '4001 South 700 East'
    prevAddress = '4001 South 700 East'
    remPackages = truck.getAllPackages()
    sum = 0.0
    while truck.getCountOfPackages() > 0:

        addressID = minDistanceFrom(address, remPackages)
        address = addressID[0]
        id = addressID[1]
        try:
            remPackages.remove(cht.search(id))
        except Exception as e:
            print('That was my final package\n')
            print('I traveled ' + str(sum) + ' miles in total.\n \n')
            
            break
        print('Delivered ' + id + ' to ' + address)
        sum = float(distanceBetween(prevAddress, address)) + sum
        prevAddress = address
        print('I have traveled: ' + str(sum) + ' miles now!\n')


addressList = addressReader()
distanceList = distanceReader()
truckOne = truck()
truckTwo = truck()
truckThree = truck()
if __name__ == '__main__':
    packageReader()
    addressReader()
    truckLoadPackages()

    truckDeliverPackages(truckOne)
    truckDeliverPackages(truckTwo)
