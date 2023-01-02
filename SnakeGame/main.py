from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game by Marek Baranski")
s.tracer(0)

snake = Snake()
FoodForSnake = Food()
Scoreboard = Scoreboard()

s.listen()
s.onkey(snake.up, "w")
s.onkey(snake.down, "s")
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")

ContinueGame = True
while ContinueGame:
    s.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with snake and food
    if snake.Head.distance(FoodForSnake) < 15:
        FoodForSnake.Refresh()
        snake.ExtendSnake()
        Scoreboard.IncreasePoints()

    # Detect collision with wall
    if snake.Head.xcor() > 285 or snake.Head.xcor() < -285 or snake.Head.ycor() > 285 or snake.Head.ycor() < -285:
        ContinueGame = False
        Scoreboard.GameOver()

    # Detect collision with tail
    for Segment in snake.Segments[1:]:
        if snake.Head.distance(Segment) < 10:
            ContinueGame = False
            Scoreboard.GameOver()


s.exitonclick()
