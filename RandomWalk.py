from turtle import *
from random import choice

#Variables and objects
LittleTurtle = Turtle()
LittleTurtle.pensize(15)
MyScreen = Screen()
MyScreen.bgcolor("black")
Colors = ["#FF8700", "#AEFF00", "#00BDFF",
          "#6800FF", "#FF0000", "#1B00FF", "#FFC500"]
Directions1 = [LittleTurtle.right, LittleTurtle.left]
Directions2 = [LittleTurtle.forward, LittleTurtle.backward]
# Option 2 
# Directions = [0, 90, 180, 270]

# MainLoop
for i in range(200):
    RandomColor = choice(Colors)
    LittleTurtle.color(RandomColor)
    RandomDirection1 = choice(Directions1)
    RandomDirection2 = choice(Directions2)
    RandomDirection1(90)
    RandomDirection2(25)
    #Option 2
    #LittleTurtle.forward(25)
    #LittleTurtle.setheading(choice(Directions))

MyScreen.exitonclick()
