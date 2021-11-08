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
        x = 1
        while x < 41:
            data_read[x].pop()
            data_read[x].pop()
            data_read[x].pop()
            data_read[x].pop()
            data_read[x].pop()
            data_read[x].pop()
            print(data_read[x])
            x += 1