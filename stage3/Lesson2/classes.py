# Lesson 3.3: Use Classes
#Draw a square, circle and triangle. Try to write code that is not repetitive.

import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,4):
        turtle.forward(320)
        turtle.left(120)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle Brad to draw a square:

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)

    #Create the turtle Angie to draw a circle:

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    #Create the turtle Todd to draw a triangle:
    todd = turtle.Turtle()
    todd.shape("arrow")
    todd.color("green")
    todd.speed(2)
    draw_triangle(todd)

    window.exitonclick()

draw_art()