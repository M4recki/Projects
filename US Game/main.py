import turtle
import pandas

s = turtle.Screen()
s.title("U. S. States Quiz Game")
s.setup(width=700, height=500)

image = r"C:\Users\marek\Documents\Prace szkolne i nie tylko\Python projects\Files (10)\US Game\blank_states_img.gif"
s.addshape(image)
turtle.shape(image)

data = pandas.read_csv(
    r"C:\Users\marek\Documents\Prace szkolne i nie tylko\Python projects\Files (10)\US Game\50_states.csv")

States = [state for state in data["state"]]

correct_guesses = 0

ContinueGame = True
while ContinueGame:
    answer_state = s.textinput(title=f"{correct_guesses}/50 States Correct",
                               prompt="What's another state's name?").capitalize()
    New_data = pandas.DataFrame(States)
    New_data.to_csv(r"C:\Users\marek\Documents\Prace szkolne i nie tylko\Python projects\Files (10)\US Game\StatesToLearn.csv")
    if answer_state in States:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        States.remove(answer_state)
        correct_guesses += 1

    if answer_state == "Exit":
        break

    if correct_guesses == 50:
        ContinueGame = False

