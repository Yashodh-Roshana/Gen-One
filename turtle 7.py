# turtle graphics
import turtle

base = 400
color = ["red", "green", "blue", "purple", "orange", "sky blue", "yellow", "white"]
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
pen = 2

for i in range(base):
    t.pensize(pen)
    pen += 0.02
    t.pencolor(color[i % len(color)])
    t.forward(i)  # make circle named forward if you like to make some tubes that will fry your cpu
    t.left(46)
