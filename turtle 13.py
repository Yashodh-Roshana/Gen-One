import turtle
# family spiral spiral goes viral
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["blue", "red", "green", "pink", "yellow", "sky blue", "grey", "white", "orange", "purple"]
base = int(turtle.numinput("Spiral goes viral", "Please tell us how many times: "))
family = []
name = name = turtle.textinput("Spriral goes viral", "Please tell a name (enter is end): ")

while name != "":
    family.append(name)
    name = turtle.textinput("Spriral goes viral", "Please tell a name (enter is end): ")

for i in range(base):
    t.color(colors[i % len(family)])
    t.penup()
    t.forward(4*i)
    t.pendown()
    t.write(family[i % len(family)], font = ("Arial", int((i+4)/4), "bold"))
    t.left(360/len(family) + 2)
