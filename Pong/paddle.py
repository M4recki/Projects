from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, Xpos, Ypos):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(Xpos, Ypos)


    def Up(self):
        NewY = self.ycor() + 20
        self.goto(self.xcor(), NewY)


    def Down(self):
        NewY = self.ycor() - 20
        self.goto(self.xcor(), NewY)