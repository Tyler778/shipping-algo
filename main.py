from hash import HashMap
from initializer import loader
import csv
from WGUhash import ChainingHashTable
from Package import Package

cht = ChainingHashTable()

truckPkgs = []

def distanceReader():
    with open("DistanceTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
        data_read.pop(0)
        distanceData = data_read
    return distanceData

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
    fromIndex = addressList.index(fromAddress)
    packageAddresses = []
    indexHold = []
    for i in truckPackages:
        packageAddresses.append(i.getAddress())
    for i in range(len(packageAddresses)):
        indexHold = addressList.index(packageAddresses[i])
    print(indexHold)
    return packageAddresses


addressList = addressReader()
distanceList = distanceReader()

if __name__ == '__main__':
    packageReader()
    addressReader()
    minDistanceFrom('3595 Main St', truckPkgs)

