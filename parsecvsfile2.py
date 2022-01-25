import csv

with open ("cvsfile2.csv") as data:

    csv_list = csv.reader(data)
    print(csv_list)
