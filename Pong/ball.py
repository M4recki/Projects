from turtle import Turtle
from math import pi, sin, cos


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.XMove = 10
        self.YMove = 10
        self.MoveSpeed = 0.1

    def MoveBall(self):

        NewX = self.xcor() + self.XMove
        NewY = self.ycor() + self.YMove
        self.goto(NewX, NewY)

    def BounceBallYPos(self):
        self.YMove *= -1

    def BounceBallXPos(self):
        self.XMove *= -1
        self.MoveSpeed *= 0.9

    def ResetPosition(self):
        self.goto(0, 0)
        self.MoveSpeed = 0.1
        self.BounceBallXPos()
