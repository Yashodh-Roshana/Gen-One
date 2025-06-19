# turtle graphics
import turtle

base = 400
red = 100
green = 75
blue = 120
t = turtle.Pen()
t.fillcolor(red / 255, green / 255, blue / 255)
turtle.bgcolor("black")
t.speed(0)

for i in range(base):
    red = 253 if red == 255 else red
    green = 253 if green == 255 else green
    blue = 250 if blue >= 254 else blue
    red += 1
    green += 0.5
    blue += 2
    t.color(red / 255, green / 255, blue / 255)
    t.forward(i)
    t.left(90.5)


