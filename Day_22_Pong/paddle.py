from turtle import Turtle


class Paddle(Turtle):
    '''For the creation of pong paddles.'''
    def __init__(self):
        super().__init__()

    def paddle(self):
        self.speed(3)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def p1_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+10)

    def p1_down(self):
        self.goto(x=self.xcor(), y=self.ycor()-10)

    def p2_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+10)

    def p2_down(self):
        self.goto(x=self.xcor(), y=self.ycor()-10)
