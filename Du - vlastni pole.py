import turtle
from math import sqrt
turtle.title("Piškvorky")
a=int(input("počet polí na šířku  - "))#počet sloupcu
b=int(input("počet polí na výšku - "))#pocet radku
strana = int(input("šírka jednoho políčka(doporučuji 50) - "))
while strana < 0 :
    print("špatný rozměr strany")
    strana = int(input(" šířka strany musí být větší než nula - "))
turtle.speed(0)
přepona=sqrt(2*(strana*strana))
cyklus=0
L=[]

for y in range(b):
    for x in range(a):
	    for i in range(4):
		    turtle.forward(strana)
		    turtle.right(90)
	    turtle.forward(strana)
    turtle.left(180)
    turtle.forward(a*strana)
    turtle.left(90)
    turtle.forward(strana)
    turtle.left(90)
turtle.setheading(0)

while cyklus<(a*b):
    if cyklus%2==0:
        print("hraje křížek")
    else:
        print("hraje kolečko")
    radek=int(input("řádek - "))
    sloupec=int(input("sloupec - " ))
    if 1<=radek<=b and 1<=sloupec<=a:
        dvojice=[radek,sloupec]
        L.append(dvojice)
        if L.count(dvojice)==1:
            tah1=(sloupec-1)*strana
            tah2=(radek-1)*strana*(-1)
            turtle.penup()
            turtle.setpos(tah1,tah2)
            turtle.pendown()
            turtle.setheading(0)        
    
            #křížek
            if cyklus%2==0 :
                turtle.color("red")
                turtle.right(45)
                turtle.forward(přepona)
                turtle.left(135)
                turtle.penup()
                turtle.forward(strana)
                turtle.pendown()
                turtle.left(135)
                turtle.forward(přepona)
                turtle.setheading(0)
                n+=1
    
            else: #kolečko
                turtle.penup()
                turtle.right(90)
                turtle.forward(strana/2)
                turtle.pendown()
                turtle.color("blue")
                turtle.circle(strana/2,360,45)
                turtle.setheading(0)
                cyklus+=1
        else:
            print("souřadnice už použity, znova")
    else:
        print("špatný vstup, znova")

print("konec")
turtle.exitonclick()
