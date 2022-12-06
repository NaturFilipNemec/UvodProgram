import csv
from datetime import datetime , timedelta
tyden_list=[]
poradi_tyden=0
List_prumer_tyden=[]
tyden_celkem = 0
rok_list=[]
rok_celkem = 0
poradi_rok=0
List_prumer_rok= []
cislo_radku = 0
Max_prutok=[]
min_prutok= []
aktualni_datum=0
with open ("vstup.csv", mode='r' , encoding="utf -8",newline='') as vstup , open('vystup_7dni.csv', mode='w',encoding="utf -8",newline='') as sedmdnu, \
     open('vystup_rok.csv', mode='w',encoding="utf -8",newline='') as rok :
        reader = csv.reader(vstup, delimiter=",")   
        writer_tyden=csv.writer(sedmdnu)
        writer_rok=csv.writer(rok)
        fieldnames_tyden = ['kod řeky','tyden' , 'prumer']
        fieldnames_rok = ['kod řeky', 'rok' , 'prumer']
        writer_rok.writerow(fieldnames_rok)
        writer_tyden.writerow(fieldnames_tyden)
        for row in reader:
            if len(row) !=4:
                raise Exception("Vstupní data nemají správný počet sloupců(4)")
            cislo_radku += 1
#vypocet maxima minima
            if len(Max_prutok)==0 and len (min_prutok)==0 :
                Max_prutok=[row[2] , row[3]]
                min_prutok=[row[2] , row[3]]
            if float(Max_prutok[1]) < float(row[3]):
                Max_prutok = [row[2], row[3]]
            if float(min_prutok[1]) > float(row[3]):
                min_prutok = [row[2] , row[3]]
            # aktualizace datumu
            if aktualni_datum == 0:
                datumicek=row[2]
                aktualni_datum = datetime.strptime(datumicek, "%d.%m.%Y").date()
            datum_radku = datetime.strptime(row[2], "%d.%m.%Y").date()
            #vypocet prumeru tydne
            #reseni děr pro tyden
            while datum_radku !=aktualni_datum:
                aktualni_datum += timedelta(days=1)
                if len(tyden_list)==0:
                    kod_reky_tyden=row[0]
                    datum_tyden = row[2]
                if len(tyden_list)<7:
                    tyden_list.append(0)
                if len(tyden_list)== 7:
                    for i in tyden_list:
                        tyden_celkem += i 
                    prumer_tyden= "{0:.4f}".format(tyden_celkem/7)
                    poradi_tyden+=1
                    pomocnej_list_tyden=[kod_reky_tyden, datum_tyden , prumer_tyden]
                    writer_tyden.writerow(pomocnej_list_tyden)
                    List_prumer_tyden.append(pomocnej_list_tyden)
                    pomocnej_list_tyden.clear()
                    tyden_list.clear()
                    tyden_celkem=0
            #bez der
            if len(tyden_list)==0:
                    kod_reky_tyden=row[0]
                    datum_tyden = row[2]
            if len(tyden_list)<7:
                tyden_list.append(float(row[3]))
            if len(tyden_list)== 7:
                for i in tyden_list:
                    tyden_celkem += i 
                prumer_tyden= "{0:.4f}".format(tyden_celkem/7)
                poradi_tyden+=1
                pomocnej_list_tyden=[kod_reky_tyden, datum_tyden , prumer_tyden]
                writer_tyden.writerow(pomocnej_list_tyden)
                List_prumer_tyden.append(pomocnej_list_tyden)
                pomocnej_list_tyden.clear()
                tyden_list.clear()
                tyden_celkem=0
#vypocet prumeru roku
#detekce děr u roka
            while datum_radku !=aktualni_datum:
                aktualni_datum += timedelta(days=1)
                if len(rok_list)==0:
                    kod_reky_rok=row[0]
                    datum_rok = row[2]
                if len(rok_list)<365:
                    rok_list.append(0)
                if len(tyden_list)== 7:
                    for i in rok_list:
                        rok_celkem += i 
                    prumer_rok= "{0:.4f}".format(rok_celkem/365)
                    poradi_rok+=1
                    pomocnej_list_tyden=[kod_reky_rok, datum_rok , prumer_rok]
                    writer_rok.writerow(pomocnej_list_rok)
                    List_prumer_rok.append(pomocnej_list_rok)
                    pomocnej_list_rok.clear()
                    rok_list.clear()
                    rok_celkem=0
            #bez der 
            if len(rok_list)==0:
                kod_reky_rok=row[0]
                datum_rok=row[2]    
            if len(rok_list)<365:
                rok_list.append(float(row[3]))
            if len(rok_list)==365:
                for i in rok_list:
                    rok_celkem+=i
                prumer_rok = "{0:.4f}".format(rok_celkem/365)
                poradi_rok+=1
                pomocnej_list_rok=[kod_reky_rok, datum_rok , prumer_rok]
                writer_rok.writerow(pomocnej_list_rok)
                List_prumer_rok.append(pomocnej_list_rok)
                pomocnej_list_rok.clear()
                rok_list.clear()
                rok_celkem=0
            #načitaní dalsiho dne pro kontrolu datumu
            if aktualni_datum == datum_radku:
                aktualni_datum+=timedelta(days=1)
              
print( "největší denní prutok byl " , Max_prutok)
print ("nejmenší denní prutok byl" ,min_prutok)

            

