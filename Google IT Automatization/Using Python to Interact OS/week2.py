#!/usr/bin/env python3
import csv
"""
file=open("week2.txt")
csv_f=csv.reader(file)
for row in csv_f:
    name,gender,salary=row
    print("Name:{},Gender:{},Salary:{}".format(name,gender,salary))
file.close()

new_employees=[["Julian","Hombre",1000],["Juana","Mujer",1200]]
with open("new.csv","w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(new_employees)
"""

#DictReader: Allows to read a csv file as a dictionary. Also exists DictWriter
with open("week2.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)
        print("{} is a {} with {} of salary".format(row["Name"],row["Gender"],row["Salary"])) #As in file

users=[{"name":"Sol","gender":"Female","salary":1500},{"name":"Luna","gender":"Female","salary":1300}]
keys=["name","gender","salary"]
with open("new.csv","w") as file:
    writer=csv.DictWriter(file,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
    print("Successfully created")