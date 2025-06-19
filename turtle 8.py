import colorsys
import turtle
# turtle graphics
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
base = 100
radius = 200


for i in range(base):
    hue = i / base
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    t.color(b, g, r)
    t.circle(radius / 2)
    t.left(47)
