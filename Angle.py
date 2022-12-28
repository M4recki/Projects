from turtle import *
from random import choice

# Variables and objects
LittleTurtle = Turtle()
MyScreen = Screen()
MyScreen.bgcolor("black")
Colors = ["#6A0000", "#000080", "#FFD700",
          "#FF1493", "#00FA9A", "#00FFFF", "#4B006A", "#FF8700"]
Division = 3

#Main loops
for i in range(8):
    Result = 360 / Division
    RandomColor = choice(Colors)
    LittleTurtle.color(RandomColor)
    Colors.remove(RandomColor)
    Division += 1
    for j in range(Division):
        LittleTurtle.forward(100)
        LittleTurtle.right(Result)
    LittleTurtle.home()

MyScreen.exitonclick()
