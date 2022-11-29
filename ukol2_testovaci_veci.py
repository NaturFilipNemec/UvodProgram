import csv
import datetime
import calendar
with open ("vstup.csv", mode='r'  encoding="utf -8",newline='') as vstup:
    tyden_list=[]
    tyden_celkem = 0
    for row in reader:
        while 7>len(tyden_list):
            tyden_list.append(row)
        for i in tyden_list:
            tyden_celkem += i
        prumer_tydem= tyden_celkem/len(tyden_list)
        print (prumer_tydem)