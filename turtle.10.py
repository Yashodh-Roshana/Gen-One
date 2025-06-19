import turtle
#rosette
t = turtle.Pen()
base = int(turtle.numinput("Rosette", "Enter Number of circles:"))
radius = int(turtle.numinput("Rosette", "Enter radius per circle:"))
turtle.bgcolor("black")
t.width(2)
t.speed(0)

for i in range(base):
    t.width(2)
    t.color("yellow")
    t.circle(radius / 2)
    t.width(1.5)
    t.color("red")
    t.circle(radius)
    t.left(360 / base)
    
