from turtle import Turtle, Screen
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()


class Board(Turtle):
    '''This creates the actual game space for the game.'''
    def __init__(self):
        super().__init__()
        screen.setup(width=800, height=600)
        screen.bgcolor("black")
        screen.title("PONG")
        scoreboard.write_score()
        self.speed(0)
        self.color("white")
        self.width(5)
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.setheading(270)
        self.setpos(0, 580)

        while self.ycor() > -500:
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()
