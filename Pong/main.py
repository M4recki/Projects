from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong game by Marek Baranski")
s.tracer(0)

RightPaddle = Paddle(Xpos=350, Ypos=0)
LeftPaddle = Paddle(Xpos=-350, Ypos=0)
LeftPaddle.color("blue")
SmallBall = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(RightPaddle.Up, "w")
s.onkey(RightPaddle.Down, "s")
s.onkey(LeftPaddle.Up, "Up")
s.onkey(LeftPaddle.Down, "Down")

ContinueGame = True

while ContinueGame:
    sleep(SmallBall.MoveSpeed)
    s.update()
    scoreboard.DrawGrid()
    SmallBall.MoveBall()

    # Detect collision wit the edge of the screen
    if SmallBall.ycor() > 280 or SmallBall.ycor() < -280:
        SmallBall.BounceBallYPos()

    # Detect collision with the paddle
    if SmallBall.distance(RightPaddle) < 50 and SmallBall.xcor() > 320 or SmallBall.distance(LeftPaddle) < 50 and SmallBall.xcor() < -320:
        SmallBall.BounceBallXPos()

    # Detect collision with the left or right wall
    if SmallBall.xcor() > 380:
        SmallBall.ResetPosition()
        scoreboard.IncreasePointForBluePlayer()

    if SmallBall.xcor() < -380:
        SmallBall.ResetPosition()
        scoreboard.IncreasePointForRedPlayer()


s.exitonclick()
