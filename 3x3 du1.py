import turtle
from math import sqrt
#nastavení
turtle.title("Piškvorky")
a=3
b=3
strana = 50
turtle.speed(0)
S=sqrt((50*50)+(50*50))
n=0
L=[]
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
while n<(a*b):
    if n%2==0: #kdo hraje
        print("hraje křížek")
    else:
        print("hraje kolečko")
        #zadavání sousřadnic
    t1=int(input("řádek(1 až 3) - "))
    t2=int(input("sloupec(1 až 3) - " ))
    #ochrana před použitím stejných vstupu
    dvojice=[t1,t2]
    L.append(dvojice)
    if L.count(dvojice) > 1 :
        print("souřadnice už použity, znova")
        continue
    else:

    #ochrana před špatnými vstupy
        if 0>t1 or t1>3 or t2 <0 or t2>3 :
            print("špatný vstup, znova")
            continue
        else:
            tah1=(t1-1)*(-50)
            tah2=(t2-1)*50
            turtle.penup()
            turtle.setpos(tah2,tah1)
            turtle.pendown()
            turtle.setheading(0)        
    
        #křížek
            if n%2==0 :
                turtle.color("red")
                turtle.right(45)
                turtle.forward(S)
                turtle.left(135)
                turtle.penup()
                turtle.forward(50)
                turtle.pendown()
                turtle.left(135)
                turtle.forward(S)
                turtle.setheading(0)
    
            else: #kolečko
                turtle.penup()
                turtle.right(90)
                turtle.forward(25)
                turtle.pendown()
                turtle.color("blue")
                turtle.circle(25,360,45)
                turtle.setheading(0)
        
        n+=1
print("konec")
turtle.exitonclick()