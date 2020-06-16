import csv


with open('C:\\BMS.csv', 'r') as f:
    reader = csv.reader(f)
    print(type(reader))
    for row in reader:
        print(row)



