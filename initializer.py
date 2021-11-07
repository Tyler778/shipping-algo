import csv

class loader:

    def distanceReader(self):
        with open("DistanceTable.csv") as dt:
            reader = csv.reader(dt,delimiter=",", quotechar='"')
            data_read = [row for row in reader]
        return data_read[20]

    def packageReader(self):
        with open("PackageTable.csv") as dt:
            reader = csv.reader(dt, delimiter=",", quotechar='"')
            data_read = [row for row in reader]
        return data_read