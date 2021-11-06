from hash import HashMap
import csv


def csvReader():
    with open("DistanceTable.csv") as dt:
        reader = csv.reader(dt, delimiter=",", quotechar='"')
        # next(reader, None)  # skip the headers
        data_read = [row for row in reader]
    return data_read[20]


if __name__ == '__main__':
    h = HashMap()

    print(csvReader())
