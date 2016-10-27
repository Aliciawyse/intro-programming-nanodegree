#Draw a flower

import turtle

def draw_pedal(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(45)
        some_turtle.forward(100)
        some_turtle.left(135)
    
        
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")

    #Create the turtle Todd to draw a pedal:
    todd = turtle.Turtle()
    todd.shape("arrow")
    todd.color("green")
    todd.speed(20)

    for i in range(36):
        draw_pedal(todd)
        todd.right(10)

    todd.right(90)
    todd.forward(250)

    window.exitonclick()


draw_flower()