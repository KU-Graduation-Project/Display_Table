import csv
import random
import time

x_value = 0
total_1 = 100
total_2 = 100
total_3 = 100
 
fieldnames = ["x_value","total_1","total_2","total_3"]
 
with open('data4.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()
while True:
    with open('data4.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
 
        info = {
            "x_value":x_value,
            "total_1":total_1,
            "total_2":total_2,
            "total_3":total_3
        }
 
        csv_writer.writerow(info)
        print(x_value,total_1,total_2,total_3)
 
        x_value += 1
        total_1 = total_1+random.randint(-4,8)
        total_2 = total_2+random.randint(-5,8)
        total_3 = total_3+random.randint(-6,8)
 
    time.sleep(1)
