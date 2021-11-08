from hash import HashMap
from initializer import loader
import csv

h = HashMap()


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
        data_read[x].pop()
        data_read[x].pop()
        data_read[x].pop()
        data_read[x].pop()
        data_read[x].pop()
        data_read[x].pop()
        h.add(data_read[x].pop(0), data_read[x])
        x += 1



if __name__ == '__main__':
    packageReader()
    h.print()
