import turtle
from math import sqrt
turtle.title("Piškvorky")
a=int(input("počet polí na šířku  - "))#počet sloupcu
b=int(input("počet polí na výšku - "))#pocet radku
strana = int(input("šírka jednoho políčka(doporučuji 50) - "))
turtle.speed(0)
S=sqrt(2*(strana*strana))
n=0
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

while n<(a*b):
    if n%2==0:
        print("hraje křížek")
    else:
        print("hraje kolečko")
    radek=int(input("řádek - "))
    sloupec=int(input("sloupec - " ))
    dvojice=[radek,sloupec]
    L.append(dvojice)
    if L.count(dvojice)==1:
        if 1<=radek<=b and 1<=sloupec<=a:
            tah1=(sloupec-1)*strana
            tah2=(radek-1)*strana*(-1)
            turtle.penup()
            turtle.setpos(tah1,tah2)
            turtle.pendown()
            turtle.setheading(0)        
    
            #křížek
            if n%2==0 :
                turtle.color("red")
                turtle.right(45)
                turtle.forward(S)
                turtle.left(135)
                turtle.penup()
                turtle.forward(strana)
                turtle.pendown()
                turtle.left(135)
                turtle.forward(S)
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
                n+=1
        else:
            print("špatný vstup, znova")
    else:
        print("souřadnice už použity, znova")

print("konec")
turtle.exitonclick()
