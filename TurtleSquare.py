from turtle import *

LittleTurtle = Turtle()
MyScreen = Screen()
MyScreen.bgcolor("black")
LittleTurtle.color("lime")
for i in range(4):
    LittleTurtle.forward(100)
    LittleTurtle.right(90)
MyScreen.exitonclick()
