import turtle
from math import sqrt
#nastavení
turtle.title("Piškvorky")
a=3
b=3
strana = 50
turtle.speed(0)
přepona=sqrt(2*(strana*strana))
#pomocný proměnný
cyklus=0
List=[]
# Nakreslí pole
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

#samotná hra
while cyklus<(a*b):
    if cyklus%2==0: #kdo hraje
        print("hraje křížek")
    else:
        print("hraje kolečko")
        #zadavání sousřadnic
    t1=int(input("řádek(1 až 3) - "))
    t2=int(input("sloupec(1 až 3) - " ))
    #ochrana před použitím stejných vstupu
    if 1<=t1<=3 and 1<=t2<=3:
        dvojice=[t1,t2]
        List.append(dvojice)
        if List.count(dvojice) == 1 :
            tah1=(t1-1)*(-1*strana)
            tah2=(t2-1)*strana
            turtle.penup()
            turtle.setpos(tah2,tah1)
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
                cyklus+=1
    
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
