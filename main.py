from hash import HashMap
from initializer import loader
import csv
from WGUhash import ChainingHashTable

h = HashMap()
cht = ChainingHashTable()

def distanceReader():
    with open("DistanceTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
    return data_read[20]


def packageReader():
    with open("PackageTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        data_read = [row for row in reader]
    x = 1
    while x < 41:
        sliced = data_read[x][0:7]
        pkg = Package(sliced[0],sliced[1],sliced[2],sliced[3],sliced[4],sliced[5],sliced[6])
        cht.insert(pkg.getId(), pkg)

        x += 1

class Package:
    def __init__(self, id, address, city, state, zip, deliveryTime, weight):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deliveryTime = deliveryTime
        self.weight = weight
    def getId(self):
        return self.id

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip

    def getDeliveryTime(self):
        return self.deliveryTime

    def getWeight(self):
        return self.weight




if __name__ == '__main__':
    packageReader()
    print(cht.search(str(12)).getAddress())

