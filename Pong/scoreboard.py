from turtle import Turtle

Position = "center"
Font = "Segoe UI Black"
Size = 70
Style = "bold"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ScoreForRedPlayer = 0
        self.ScoreForBluePlayer = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.UpdateScoreboard()


    def UpdateScoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.color("blue")
        self.write(self.ScoreForBluePlayer, align=Position, font=(Font, Size, Style))
        self.goto(100, 200)
        self.color("red")
        self.write(self.ScoreForRedPlayer, align=Position, font=(Font, Size, Style))

    
    def IncreasePointForRedPlayer(self):
        self.ScoreForRedPlayer += 1
        self.UpdateScoreboard()

    def IncreasePointForBluePlayer(self):
        self.ScoreForBluePlayer += 1
        self.UpdateScoreboard()

