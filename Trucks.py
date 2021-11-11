from Package import Package
#from main import addressList
import datetime


class truck:
    def __init__(self):
        self.packages = []
        self.addressVisited = []
        self.allAddresses = []
        self.count = 0
        self.finishTime = None
        self.returnHubTime = None
        self.milesTraveled = None
        self.milesTraveledHub = None

    def load(self, package):
        self.allAddresses.append(package.getAddress())
        if self.count < 16:
            self.packages.append(package)
            self.count += 1
        else:
            print("truck has max packages")

        if (package.getAddress() not in self.addressVisited):
            self.addressVisited.append(package.getAddress())


    def printPackageIDs(self):
        for i in self.packages:
            print(i.getId())
    def printAddress(self):
        for i in self.addressVisited:
            print(i)
    def getAllAddresses(self):
        return self.allAddresses
    def getAllPackages(self):
        return self.packages

    def getCountOfPackages(self):
        return self.count
    def getStops(self):
        print(len(self.addressVisited))

    def setFinishTime(self, ft):
        self.finishTime = ft

    def getFinishTime(self):
        return self.finishTime
    def setReturnHubTime(self, rht):
        self.returnHubTime = rht
    def getReturnHubTime(self):
        return self.returnHubTime
    def setMilesTraveled(self, miles):
        self.milesTraveled = miles
    def getMilesTraveled(self):
        return self.milesTraveled
    def removePackageCount(self):
        self.count = self.count - 1

