import csv
tyden_list=[]
tyden_celkem = 0
rok_list=[]
rok_celkem = 0
List_T=[]
List_R=[]
def dokument():
    with open ("vstup.csv", encoding="utf -8",newline='')as vstup,  open('vystup_7dni.csv', mode='w',encoding="utf -8",newline='') as sedmdnu,  \
     open('vystup_rok', mode='w',encoding="utf -8",newline='') as rok :
            reader = csv.DictReader(vstup, delimiter=";")   
            next(reader) #uvedom si jak vypada prvni radek
            writer1=csv.writer(sedmdnu)
            writer2=csv.writer(rok)

def sedm_dnu(): #vypocet prumeru
    for row in reader:
        while 7 > len(tyden_list):
            if row["datum"] -1  == row ["datum"+1]:     #vyresit jak zadat aby se preskocili mezery mezi datumy(tohle nevim jestli funguje )
                tyden_list.append ( row["prutok"] )     # zjistit jak se jmenuje den radek s prutokem
        for i in tyden_list:
             tyden_celkem += i
        prumer_tydem= tyden_celkem/len(tyden_list)  # doplnit zapsanej dokument vyresit to 
        return(prumer_tydem)
        print(prumer_tydem)
        List_T.append(prumer_tydem)
    PoradiTyden=[]
    for i in range(len(List_T)):
        PoradiTyden.append(i)
    writer1=csv.writer(sedmdnu) 
    fieldnames = ['tyden' , 'prumer']
    writer1.writerow(fieldnames)
    for row in reader:            
            name=row['reka']        #tady taky vyresit jmena 
            capa=row['prumer']
            outrow = [name , capa]
            writer1.writerow(outrow)

def rok_prumer():
    for row in reader:
        while 365 > len (rok_list):
            if row["datum"]-1 == row["datum"+1]:        # vyresit stejne jako u tejdnu
                rok_list.append(row["prutok"])
        for i in rok_list:
            rok_celkem += i 
        prumer_rok= rok_celkem / len(rok_list)
        return(prumer_rok)
        print(prumer_rok)
            

