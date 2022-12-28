from turtle import *

LittleTurtle = Turtle()
MyScreen = Screen()
MyScreen.bgcolor("black")
LittleTurtle.color("lime")
for i in range(50):
    LittleTurtle.forward(10)
    LittleTurtle.pendown()
    LittleTurtle.forward(10)
    LittleTurtle.penup()
