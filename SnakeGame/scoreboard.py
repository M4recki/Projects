from turtle import Turtle

Position = "center"
Font = "Segoe UI Black"
Size = 24
Style = "bold"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 260)
        self.write("Score: {}".format(self.score),
                   align=Position, font=(Font, Size, Style))

    def IncreasePoints(self):
        self.clear()
        self.score += 1
        self.write("Score: {}".format(self.score),
                   align=Position, font=(Font, Size, Style))

    def GameOver(self):
        self.goto(0, 0)
        self.write("Game Over".format(self.score),
                   align=Position, font=(Font, Size, Style))
