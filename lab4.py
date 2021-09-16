


######################################################
# Assignment: Lab 4
# UIN: <679663325>
# Name: <Xiangcheng Li>
######################################################
 
 
# DONE: import the turtle package
import turtle
 
# DONE: create a new turtle and assign to variable t1
t1 = turtle.Turtle()
 
# DONE: create another turtle and assign to variable t2
t2 = turtle.Turtle()
 
 
# DONE: write the commands to draw a filled rectangle 75 x 25 
# length = 75
# width = 25
# angle = 90

# t1.color("red")
# t1.begin_fill()
# for i in range(2):
#   t1.forward(width)
#   t1.left(angle)
#   t1.forward(length)
#   t1.left(angle)
# t1.end_fill()

# reminder to test and save often
 
 
# DONE: create a function named draw_rectangle and move the above commands into it
# def draw_rectangle(length, width, angle):
#   t1.color("orange")
#   t1.begin_fill()
#   for i in range(2):
#     t1.forward(width)
#     t1.left(angle)
#     t1.forward(length)
#     t1.left(angle)
#   t1.end_fill()
 
 
# DONE: uncomment the following line to test your function
# draw_rectangle(75,25,90)
 
 
# TODO: update the function to accept a parameter for the turtle
#       as you create each new version, comment out the prior version
# def draw_rectangle(turtle,length, width, angle):
#   turtle.color("orange")
#   turtle.begin_fill()
#   for i in range(2):
#     turtle.forward(width)
#     turtle.left(angle)
#     turtle.forward(length)
#     turtle.left(angle)
#   turtle.end_fill()
 
 
 
# TODO:  uncomment the following lines to test your function
# draw_rectangle (t1,75,25,90)
# draw_rectangle (t2,75,25,90)
 
 
# TODO: update the function to accept parameters for length and width
# def draw_rectangle(turtle,length, width, angle):
#   turtle.color("orange")
#   turtle.begin_fill()
#   for i in range(2):
#     turtle.forward(width)
#     turtle.left(angle)
#     turtle.forward(length)
#     turtle.left(angle)
#   turtle.end_fill()
 
 
# TODO:  uncomment the following line to test your function
# draw_rectangle (t2, 50, 100)
# draw_rectangle (t1, 10, 20)
 
# reminder to save often
 
 
# TODO: update your function to accept a parameter for color
# def draw_rectangle(turtle,length, width, color):
#   turtle.color(color)
#   turtle.begin_fill()
#   for i in range(2):
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#   turtle.end_fill()
 
# TODO: uncomment the lines below to test your updated function;
#       you should see a red square and a blue square
# draw_rectangle (t1, 50, 50, "red")
# draw_rectangle (t2, 10, 30, "blue")
 
 
 
# TODO: update your function to accept x and y coordinates;
#       you'll need to use the 'goto" method in your function
#       the x and y coordinates will be the second and third parameters
# def draw_rectangle(turtle,x,y,length, width, color):
#   turtle.color(color)
#   turtle.penup()
#   turtle.goto(x,y)
#   turtle.pendown()
#   turtle.begin_fill()
#   for i in range(2):
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#   turtle.end_fill()
 
 
 
# TODO: uncomment the following line to test your function;
# draw_rectangle (t1, -25, -50, 25, 100, "blue")
# draw_rectangle (t2, 50, 50, 30, 30, "green")
 
 
# TODO: update your function to accept a parameter for heading and pensize
#       these should be at the end of the parameter list
def draw_rectangle(turtle,x,y,length, width, color, heading, pensize):
  turtle.left(90)
  turtle.color(color)
  turtle.pensize(pensize)
  turtle.left(heading)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
  turtle.end_fill()
  turtle.hideturtle()
 
 
# TODO: uncomment the following lines to test your function
 
draw_rectangle (t1, 50, -50, 75, 15, "green", 45, 2)
draw_rectangle (t2, 0, 0, 30, 75, "orange", 0, 10)
draw_rectangle (t2, 100, 100, 25, 25, "purple", 75, 5)
 
 
# TODO:  use the turtle "write" method to write your UIN and name
#        write them at x = -100, y = 100
t1.penup()
t1.goto(-100,100)
t1.pendown()
t1.write("Xiangcheng Li - 679663325 ",
         move=False, align='left',
         font=('Arial', 8, 'normal'))
#        here are two resources
#        https://www.geeksforgeeks.org/turtle-write-function-in-python/
#        https://docs.python.org/3/library/turtle.html#turtle.write
