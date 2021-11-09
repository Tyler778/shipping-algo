from Package import Package
#from main import addressList

class truck:
    def __init__(self):
        self.packages = []
        self.addressVisited = []
        self.count = 0

    def load(self, package):
        if self.count < 20:
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


    def getCountOfPackages(self):
        print(self.count)
    def getStops(self):
        print(len(self.addressVisited))