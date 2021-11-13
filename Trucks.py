

# Class truck holds info such as packages, specific addresses to be delivered, as well as the count of current packages.
class truck:
    # Constructor
    def __init__(self):
        self.packages = []
        self.addressVisited = []
        self.allAddresses = []
        self.count = 0
        self.milesTraveled = None



    # Method called to load package object into packages[] as well as increment the count.
    #
    # Time and space complexity of O(1)
    def load(self, package):
        self.allAddresses.append(package.getAddress())
        if self.count < 16:
            self.packages.append(package)
            self.count += 1
        else:
            print("truck has max packages")

        if (package.getAddress() not in self.addressVisited):
            self.addressVisited.append(package.getAddress())

    #Getters and setters for attributes within the Truck class
    #
    # No complexity higher than O(1)
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

