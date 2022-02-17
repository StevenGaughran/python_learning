from turtle import Turtle

ALIGNMENT = (0, 0)
FONT = ("Arial", 50, "center")


class Scoreboard(Turtle):
    '''This creates the scoreboard for the game.'''
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.p1_points = 0
        self.p2_points = 0
        self.write_score()

    def write_score(self):
        self.setpos(-50, 200)
        self.write(f"{self.p1_points}", align="center", font=("Arial", 50, "bold"))
        self.setpos(50, 200)
        self.color("white")
        self.write(f"{self.p2_points}", align="center", font=("Arial", 50, "bold"))

    def p1_scores(self):
        self.p1_points += 1
        self.clear()
        self.write_score()

    def p2_scores(self):
        self.p2_points += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", font=FONT)
