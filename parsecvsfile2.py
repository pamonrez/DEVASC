import csv

with open ("cvsfile2.csv") as data:

    csv_list = csv.reader(data)
    csv_lst = list(csv_list)
    print(csv_lst)
    
