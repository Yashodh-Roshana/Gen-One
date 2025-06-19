# turtle graphics
import turtle

base = 200
red = 0
green = 0
blue = 0

t = turtle.Pen()
t.fillcolor("#000000")
t.speed(0)

for i in range(base):
    red = 253 if red == 255 else red
    green = 253 if green == 255 else green
    blue = 250 if blue >= 254 else blue
    red += 1
    green += 0.5
    blue += 2
    t.pensize(1.5)
    t.color(red / 255, green / 255, blue / 255)
    t.forward(0.8*i)
    t.left(75)


