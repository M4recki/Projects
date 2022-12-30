from turtle import Turtle, Screen
from random import randint

Colors = ["red", "green", "orange", "yellow", "blue", "purple"]
Turtles = []

s = Screen()
s.setup(width=500, height=400)
s.bgcolor("black")
UserChoice = s.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

if UserChoice not in Colors:
    print("You have entered incorrect color.")
    quit()

PositionX = -230
PositionY = -100

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(Colors[i])
    t.penup()
    t.goto(x=PositionX, y=PositionY)
    PositionY += 40
    Turtles.append(t)

StartRace = False

if UserChoice:
    StartRace = True

while StartRace:
    for t in Turtles:
        if t.xcor() > 230:
            StartRace = False
            Winner = t.pencolor()
            if Winner == UserChoice:
                print(f"You have won! The {Winner} turtle is a winner!")
            else:
                print(f"You have lost! The {Winner} turtle is a winner!")
        RandomSpeed = randint(0, 10)
        t.forward(RandomSpeed)


s.exitonclick()
