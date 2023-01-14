from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(-220, 240)
        self.write("Level {}".format(self.level), align="center", font=FONT)

    def IncreaseLevel(self):
        self.clear()
        self.goto(-220, 240)
        self.level += 1
        self.write("Level {}".format(self.level), align="center", font=FONT)

    def GameOver(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)

