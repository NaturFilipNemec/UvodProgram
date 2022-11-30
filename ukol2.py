import csv
tyden_list=[]
tyden_celkem = 0
rok_list=[]
rok_celkem = 0
aktualni_rok = 0
cislo_radku = 0
Max_prutok=[]
min_prutok= []
with open ("vstup.csv", mode='r' , encoding="utf -8",newline='') as vstup , open('vystup_7dni.csv', mode='w',encoding="utf -8",newline='') as sedmdnu, \
     open('vystup_rok.csv', mode='w',encoding="utf -8",newline='') as rok :
        reader = csv.reader(vstup, delimiter=",")   
        writer_tyden=csv.writer(sedmdnu)
        writer_rok=csv.writer(rok)
        for row in reader:
            if len(row) !=4:
                raise Exception("Vstupní data nemají správný počet sloupců(4)")
            cislo_radku += 1
            if len(Max_prutok)==0 and len (min_prutok)==0 :
                Max_prutok=[row[2] , row[3]]
                min_prutok=[row[2] , row[3]]
            if float(Max_prutok[1]) < float(row[3]):
                Max_prutok = [row[2], row[3]]
            if float(min_prutok[1]) > float(row[3]):
                min_prutok = [row[2] , row[3]]
print( Max_prutok)
print (min_prutok)

            

