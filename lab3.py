import turtle
s = turtle.Screen()
s.setup(width=500, height=500)
s.bgcolor("silver")

student_uin = "679663325"

color1 = "red"
color2 = "yellow"
color3 = "green"
color4 = "blue"
color5 = "purple"

t1 = turtle.Turtle()

t1.penup()
t1.goto(-200,200)
t1.write("Lab 3 - " + student_uin,
         move=False, align='left',
         font=('Arial', 24, 'normal'))

t1.penup()
t1.goto(-200,0)
t1.pendown()

dis = 10
angle = 120

t1.color("red")
t1.begin_fill()
t1.penup()
t1.forward(dis)
t1.pendown()
for i in range(3):
    t1.forward(dis)
    t1.left(angle)
t1.end_fill()

dis = dis * 2

t1.color("yellow")
t1.begin_fill()
t1.penup()
t1.forward(10)
t1.pendown()
for i in range(3):
    t1.forward(dis)
    t1.left(angle)
t1.end_fill()

dis = dis * 2

t1.color("blue")
t1.begin_fill()
t1.penup()
t1.forward(20)
t1.pendown()
for i in range(3):
    t1.forward(dis)
    t1.left(angle)
t1.end_fill()

dis = dis * 2

t1.color("green")
t1.begin_fill()
t1.penup()
t1.forward(40)
t1.pendown()
for i in range(3):
    t1.forward(dis)
    t1.left(angle)
t1.end_fill()

dis = dis * 2

t1.color("pink")
t1.begin_fill()
t1.penup()
t1.forward(80)
t1.pendown()
for i in range(3):
    t1.forward(dis)
    t1.left(angle)
t1.end_fill()

t1.hideturtle()