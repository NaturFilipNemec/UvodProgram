import csv
from datetime import datetime , timedelta
tyden_list=[]
List_prumer_tyden=[]
tyden_celkem = 0
rok_list=[]
rok_celkem = 0
List_prumer_rok= []
Max_prutok=[]
min_prutok= []
aktualni_datum=0
chybejici_datumy=[]
zaporne_prutoky=[]
aktualni_tyden=0
aktualni_rok=0
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
            # aktualizace datumu
            if aktualni_datum == 0:
                datumicek=row[2]
                aktualni_datum = datetime.strptime(datumicek, "%d.%m.%Y").date()
            datum_radku = datetime.strptime(row[2], "%d.%m.%Y").date()
            #zaporny prutok
            if float(row[3])<0:
                zaporne_prutoky.append([aktualni_datum, row[3]])
                if aktualni_datum == datum_radku:
                    aktualni_datum+=timedelta(days=1)
                    continue
#vypocet maxima minima
            if len(Max_prutok)==0 and len (min_prutok)==0 :
                Max_prutok=[row[2] , row[3]]
                min_prutok=[row[2] , row[3]]
            if float(Max_prutok[1]) < float(row[3]):
                Max_prutok = [row[2], row[3]]
            if float(min_prutok[1]) > float(row[3]):
                min_prutok = [row[2] , row[3]]
##tyden
            if aktualni_tyden==0:
                aktualni_tyden=datetime.strptime(row[2], "%d.%m.%Y").date()
            #vypocet prumeru tydne
            #reseni děr pro tyden
            while datum_radku !=aktualni_datum:
                chybejici_datumy.append(str(aktualni_datum))#chybejici datumy
                aktualni_datum += timedelta(days=1)
                if len(tyden_list)==0:
                    kod_reky_tyden=row[0]
                    datum_tyden = row[2]
                if len(tyden_list)<7:
                    tyden_list.append(0)
                if len(tyden_list)==7:
                    for i in tyden_list:
                        tyden_celkem += i 
                    nuly=tyden_list.count(0)
                    prumer_tyden= "{0:.4f}".format(tyden_celkem/(len(tyden_list)-nuly))
                    pomocnej_list_tyden=[kod_reky_tyden, datum_tyden , prumer_tyden]
                    writer_tyden.writerow(pomocnej_list_tyden)
                    List_prumer_tyden.append(pomocnej_list_tyden)
                    pomocnej_list_tyden.clear()
                    tyden_list.clear()
                    tyden_celkem=0
                    aktualni_tyden = 0                    
            #bez der
            if len(tyden_list)==0:
                    kod_reky_tyden=row[0]
                    datum_tyden = row[2]
            if len(tyden_list)<7:
                tyden_list.append(float(row[3]))
            if len(tyden_list)==7:
                for i in tyden_list:
                    tyden_celkem += i 
                nuly=tyden_list.count(0)
                prumer_tyden= "{0:.4f}".format(tyden_celkem/(len(tyden_list)-nuly))
                pomocnej_list_tyden=[kod_reky_tyden, datum_tyden , prumer_tyden]
                writer_tyden.writerow(pomocnej_list_tyden)
                List_prumer_tyden.append(pomocnej_list_tyden)
                pomocnej_list_tyden.clear()
                tyden_list.clear()
                tyden_celkem=0
                aktualni_tyden=0
##ROK
            if aktualni_rok == 0:
                aktualni_rok =datetime.strptime(row[2], "%d.%m.%Y").date()

#vypocet prumeru roku
#detekce děr u roka
            while datum_radku !=aktualni_datum:
                aktualni_datum += timedelta(days=1)
                if len(rok_list)==0:
                    kod_reky_rok=row[0]
                    datum_rok = row[2]
                if aktualni_rok.year == aktualni_datum.year :
                    continue
                if aktualni_rok.year != aktualni_datum.year :
                    for i in rok_list:
                        rok_celkem += i 
                    prumer_rok= "{0:.4f}".format(rok_celkem/len(rok_list))
                    pomocnej_list_rok=[kod_reky_rok, datum_rok , prumer_rok]
                    writer_rok.writerow(pomocnej_list_rok)
                    List_prumer_rok.append(pomocnej_list_rok)
                    pomocnej_list_rok.clear()
                    rok_list.clear()
                    if len(rok_list)==0:
                        kod_reky_rok=row[0]
                        datum_rok=row[2]
                        rok_list.append(float(row[3]))
                    rok_celkem=0
                    aktualni_rok=0
            #bez der 
            if len(rok_list)==0:
                kod_reky_rok=row[0]
                datum_rok=row[2]             
            if aktualni_rok.year == aktualni_datum.year :
                rok_list.append(float(row[3]))
            if aktualni_rok.year != aktualni_datum.year :
                for i in rok_list:
                    rok_celkem+=i
                prumer_rok = "{0:.4f}".format(rok_celkem/len(rok_list))
                pomocnej_list_rok=[kod_reky_rok, datum_rok , prumer_rok]
                writer_rok.writerow(pomocnej_list_rok)
                List_prumer_rok.append(pomocnej_list_rok)
                pomocnej_list_rok.clear()
                rok_list.clear()
                if len(rok_list)==0:
                    kod_reky_rok=row[0]
                    datum_rok=row[2]
                    rok_list.append(float(row[3]))
                rok_celkem=0
                aktualni_rok=0
            #načitaní dalsiho dne pro kontrolu datumu
            if aktualni_datum == datum_radku:
                aktualni_datum+=timedelta(days=1)
            
              
print("hotovo, průměry týdnů jsou v dokumentu vystup_7dni.csv a průměry roků jsou v dokumentu vystup_rok.csv")
print( "největší denní prutok byl " , Max_prutok)
print ("nejmenší denní prutok byl" ,min_prutok)
if zaporne_prutoky!=[]:
    print ("chybna data. Zaporné prutoky - " , zaporne_prutoky)
if chybejici_datumy != []:
    print("chybejici datumy jsou - ", chybejici_datumy)


            

