FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.hideturtle()
        self.penup()
        self.setpos(0, 245)
        self.write_score()

    def write_score(self):
        self.write(f"Level {self.player_score + 1}", align="center", font=FONT)

    def score_point(self):
        self.player_score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
