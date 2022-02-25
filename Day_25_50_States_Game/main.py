import pandas
import turtle

screen = turtle.Screen()
t = turtle.Turtle()


screen.title("US States Game!")
screen.setup(725, 491)

screen.addshape("./blank_states_img.gif")
t.shape("./blank_states_img.gif")

guesses = 0

states_data = pandas.read_csv("./50_states.csv")
states_list = states_data.state.to_list()
score = 0

guessed_states = []

game_on = True
while game_on and score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="List a state!").title()

    if answer_state == "Exit":
        missed_states = []
        for i in states_list:
            if i not in guessed_states:
                missed_states.append(i)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        score += 1
        guessed_states.append((answer_state))
        guessed_state = states_data[states_data.state == answer_state]
        author = turtle.Turtle()
        author.penup()
        author.hideturtle()
        author.goto(int(guessed_state.x), int(guessed_state.y))
        author.write(arg=answer_state)

screen.exitonclick()
