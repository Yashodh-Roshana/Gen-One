import colorsys
import turtle
# turtle graphics
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
base = int(turtle.numinput("Circles", "Enter amount of circles: "))
radius = int(turtle.numinput("Circles", "Enter radius per circle: "))


while True:
    for i in range(base):
        hue = i / base
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(b, g, r)
        t.circle(radius / 2)
        t.left(360 / base)
