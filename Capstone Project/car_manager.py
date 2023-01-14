from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.Cars = []

    def CreateCars(self):
        Random_Chance = randint(1, 6)
        if Random_Chance == 1:
            NewCar = Turtle("square")
            NewCar.shapesize(stretch_wid=1, stretch_len=2)
            NewCar.penup()
            NewCar.color(choice(COLORS))
            RandomY = randint(-250, 250)
            NewCar.goto(300, RandomY)
            self.Cars.append(NewCar)

    def MoveCars(self):
        for Car in self.Cars:
            Car.backward(STARTING_MOVE_DISTANCE)
        
    def IncreaseSpeed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT