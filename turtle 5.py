# turtle graphics
import turtle

base = 100
t = turtle.Pen()
t.fillcolor("#000000")
t.speed(0)

for i in range(base):
    t.circle(i)
    t.left(60)

