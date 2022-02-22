from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        finish_line = FINISH_LINE_Y
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.setposition(STARTING_POSITION)

    def move(self):
        self.goto(x=self.xcor(), y=self.ycor() + MOVE_DISTANCE)
