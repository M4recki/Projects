from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#FF4B4B")
        self.speed("fastest")
        self.Refresh()
    
    def Refresh(self):
        RandomX = randint(-280, 280)
        RandomY = randint(-280, 280)
        self.goto(RandomX, RandomY)