#Drawing turtles practice

#Inside the python standard library there is a file called turtle. 
#Inside that file is a class Turtle. A class is a neatly packaged box.
#It allows us to write code like turtle.Turtle() as if we were writing a funciton.
#When we run this code, we call a function called Init, initialize, that creates
#space in memory for a new object of the class turtle.  

import turtle

def draw_square_and_circle():
    window = turtle.Screen()
    window.bgcolor("red")
    
    count = 0
    while count < 4:
        turtle.position()
        turtle.forward(100)
        turtle.right(90)
        count = count + 1
    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    
    todd = turtle.Turtle()
    todd.shape("arrow")
    todd.color("green")
    
    todd_count = 0
    whilte todd_count < 3:
        todd.forward(300)
        todd.left(120)
        todd_count = todd_count + 1
    
    window.exitonclick()

draw_square_and_circle()

#What is a class and an instance?

#A class is like a blueprint of a building. It contains the information about the nuts and bolts about the building. (height, number of rooms) It can be used for different types of "buildings" such as an office building or residential building.

#We can use this blueprint and create diff examples of it.

#A class turtle, like a blueprint, contains info about the size, color, turn right, left. From this class, we can create multiple instances of it. 