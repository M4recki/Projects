from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Capstone project by Marek Baranski")

player = Player()

screen.listen()
screen.onkey(player.move_forward, "w")

scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True

while game_is_on:
    sleep(0.1)
    screen.update()

    car_manager.CreateCars()
    car_manager.MoveCars()

    # Detect collision
    for car in car_manager.Cars:
        if player.distance(car) < 20:
            scoreboard.GameOver()
            game_is_on = False

    # crossed the street
    if player.ycor() >= 280:
        player.ResetPlayerPosition()
        scoreboard.IncreaseLevel()
        car_manager.IncreaseSpeed()

screen.exitonclick()
