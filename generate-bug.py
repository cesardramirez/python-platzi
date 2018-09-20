import turtle
import math as mt

a=200
b=5
a1=[]
b1=[]
c=[]
f1=[]
f2=[]
for s in range(0,40):
	a1.append(a)
	b1.append(b)
	a=a-5
	b=b+5
for e in range(0,40):
	q=((a1[e]**2)+(b1[e]**2))**(1/2)
	c.append(q)
for g in range(0,40):
    q=((mt.asin(b1[g]/c[g]))*180)/mt.pi
    f1.append(q)
    q1=((mt.asin(a1[g]/c[g]))*180)/mt.pi
    f2.append(q1)
a1.append(5)
window = turtle.Screen()
alejo = turtle.Turtle()
alejo.forward(200)
alejo.left(90)
alejo.forward(200)
for w in range(0,40):
	alejo.left(f2[w])
	alejo.forward(c[w])
	alejo.left(f1[w])
	alejo.forward(b1[w])
	alejo.left(90)
	alejo.forward(a1[w+1])
alejo.forward(200)
alejo.left(90)
alejo.forward(205)
alejo.left(90)
alejo.forward(205)
alejo.left(90)
alejo.forward(205)

turtle.mainloop()