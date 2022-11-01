import turtle
from math import sqrt
turtle.title("Piškvorky")
a=int(input("počet polí na šířku  - "))
b=int(input("počet polí na výšku - "))
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
    t1=int(input("řádek - "))
    t2=int(input("sloupec - " ))
    dvojice=[t1,t2]
    L.append(dvojice)
    if L.count(dvojice)>1:
        print("souřadnice už použita, znova")
        continue
    else:
        if 0>t1 or t1>a or t2 <0 or t2>b :
            print("špatný vstup, znova")
            continue
        else:
            tah1=(t1-1)*(-50)
            tah2=(t2-1)*50
            turtle.penup()
            turtle.setpos(tah2,tah1)
            turtle.pendown()
            turtle.setheading(0)
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
            else:
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