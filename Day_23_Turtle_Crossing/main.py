import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()
    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        scoreboard.score_point()
        player.goto(0, -280)
        car.speed_up()


screen.exitonclick()
