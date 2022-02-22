COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y_cor = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=random.randint(1, 3))
            new_car.color(random.choice(COLORS))
            new_car.setpos(300, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
