import turtle
import pandas

data = pandas.read_csv('50_states.csv')
state_list = data['state'].to_list() #adds all states in a list


screen = turtle.Screen()
screen.title(f'US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)


guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(f'{len(guessed_states)}/50 States Correct', "What's another state name?").strip().title()

    # exiting loop when exit is entered
    if user_answer == 'Exit':
        states_left = [state for state in state_list if state not in guessed_states]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0,0)
        t.shapesize(2.5, 2.5)
        df = pandas.DataFrame(states_left)
        df.to_csv('states_to_learn.csv')
        t.write(f'You missed {len(states_left)} states!', align='center', font=['Fira Code', 20, 'bold'])
        break

    # checking user answer
    if user_answer in state_list and user_answer not in guessed_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        state_x, state_y = int(state_data.x), int(state_data.y)
        t.goto(state_x, state_y)
        t.write(user_answer)
else:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0,0)
    t.shapesize(2.5, 2.5)
    t.write('Well Done!', align='center', font=['Fira Code', 20, 'bold'])


screen.exitonclick()
     