import csv
tyden_list=[]
def dokument():
    with open ("vstup.csv", encoding="utf -8",newline='')as vstup,  open('vystup_7dni.csv', mode='w',encoding="utf -8",newline='') as sedmdnu,  \
     open('vystup_rok', mode='w',encoding="utf -8",newline='') as rok :
            reader = csv.DictReader(vstup, delimiter=";")   
            next(reader) #uvedom si jak vypada prvni radek
            writer1=csv.writer(sedmdnu)
            writer2=csv.writer(rok)
def sedm_dnu():
    for row in reader:
        while tyden_list < len(tyden_list):
            if row["datum"] -1  == row ["datum"+1]
            tyden_list.append ( row["prutok"] )     # zjistit jak se jmenuje den radek s prutokem

