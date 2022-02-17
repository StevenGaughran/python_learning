import time
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
scoreboard = Scoreboard()
t = Turtle()
t.hideturtle()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
t.speed(0)
t.color("white")
t.width(5)
t.penup()
t.shape("square")
t.setheading(270)
t.setpos(0, 300)

while t.ycor() > -300:
    t.forward(20)
    t.pendown()
    t.forward(20)
    t.penup()

player_1 = Paddle()
player_2 = Paddle()
ball = Ball()
player_1.paddle()
player_1.goto(-350, 0)
player_2.paddle()
player_2.goto(350, 0)

screen.listen()
screen.onkey(key="Up", fun=player_2.p2_up)
screen.onkey(key="Down", fun=player_2.p2_down)

screen.onkey(key="w", fun=player_1.p1_up)
screen.onkey(key="s", fun=player_1.p1_down)


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    if ball.distance(player_1) < 50 and ball.xcor() > -340:
        ball.bounce_x()
    elif ball.distance(player_2) < 50 and ball.xcor() > 340:
        ball.bounce_x()

    if ball.xcor() > 400:
        scoreboard.p1_scores()
        ball.home()
    elif ball.xcor() < -400:
        scoreboard.p2_scores()
        ball.home

screen.exitonclick()
