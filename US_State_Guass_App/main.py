import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

'''def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
'''
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",
                                    prompt="what's another stats name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        #t.write(state_data.state.item())
        t.write(answer_state)






#turtle.mainloop()
#screen.exitonclick()