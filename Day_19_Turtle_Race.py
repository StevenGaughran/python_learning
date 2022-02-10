# Day 19. Today's exercise was more of a follow-along sort of thing. Using Turtle isn't too difficult, but I feel
# like I really need to brush up on my "for/in" loops. I keep doing things "long-hand", as it were, which works?
# But it also takes a lot longer.

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

prediction = screen.textinput(title="Place your bets!", prompt="Which turtle will win the race? Enter a color: ")

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)
    # Using the turtle_index number to pull from lists was the teacher's idea, and it's very clever.
    # It took me a hot minute to figure what was going on, because she didn't actually explain how/why it was working.
    # Appending the list with the "new turtle" was a bit confusing.
    # I see after printing it up that it makes a "turtle object" at a memory location. Didn't know you could do that.

print(turtles)

if prediction:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == prediction:
                print(f"You win! {winning_color} is the winner.")
            else:
                print(f"You lose! {winning_color} is the winner.")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

# I feel like this file is not properly set up, but I'm just following along.
# So it goes.
























screen.exitonclick()