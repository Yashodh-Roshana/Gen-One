# turtle graphics
import turtle

base = 1000
t = turtle.Pen()
t.speed(0)


for i in range(base):
    t.forward(i)
    t.left(90)