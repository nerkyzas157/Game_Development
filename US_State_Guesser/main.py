import pandas  # type: ignore
import turtle

screen = turtle.Screen()
screen.title("U.S. Quiz Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()


data = pandas.read_csv("50_states.csv")

correct_guesses = 0
guesses = []

while correct_guesses < 50:
    if correct_guesses == 0:
        answer_state = screen.textinput(
            title="Guess The State",
            prompt="Guess state's name?",
        ).title()
    else:
        answer_state = screen.textinput(
            title=f"{correct_guesses}/50 States Guessed Correctly",
            prompt="Guess another state's name?",
        ).title()
    for i in data["state"]:
        if answer_state not in guesses and i == answer_state:
            data_list = data[data["state"] == i].values.tolist()
            state = turtle.Turtle()
            state.shape("circle")
            state.shapesize(stretch_len=0.15, stretch_wid=0.15)
            state.penup()
            state.goto(data_list[0][1], data_list[0][2])
            state.pendown()
            state.write(
                f"{data_list[0][0]}",
                move=False,
                align="center",
                font=("Courier", 8, "normal"),
            )
            correct_guesses += 1
            guesses.append(answer_state)
    if answer_state == "Exit":
        for d in data["state"]:
            if d not in guesses:
                data_list = data[data["state"] == d].values.tolist()
                state = turtle.Turtle()
                state.shape("circle")
                state.shapesize(stretch_len=0.15, stretch_wid=0.15)
                state.penup()
                state.goto(data_list[0][1], data_list[0][2])
                state.pendown()
                state.write(
                    f"{data_list[0][0]}",
                    move=False,
                    align="center",
                    font=("Courier", 8, "normal"),
                )
        try_again = screen.textinput(
            title="Game Over",
            prompt="Would you like to try again?",
        ).title()
        if try_again == "Yes":
            correct_guesses = 0
            guesses = []
            screen.clearscreen()
            turtle.shape(image)
        else:
            break


screen.exitonclick()
