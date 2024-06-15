import turtle
import pandas
screen = turtle.Screen()
# -----------------------------  This makes it fullscreen   -------------------------------
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
#------------------------------------------------------------------------------------------
screen.title("States game")
image = "bg.gif"
screen.addshape(image)
turtle.shape(image)
# cursor.penup()
#------------------------------------------------------------------------------------------
# Funciton to get coordinates of the states on click and adding them to an external file.
# def get_coordinates_and_name(x,y):
#     name = screen.textinput(title="Coordinates jama karing", prompt="Write a state's name:")
#     file = open("coordinates.csv", "a")
#     s = name + "," +str(x)+","+str(y)+"\n"
#     file.write(s)
# turtle.onscreenclick(get_coordinates_and_name)
# turtle.mainloop()
#------------------------------------------------------------------------------------------

data = pandas.read_csv("coordinates.csv")
states = list(data.state)
guessed_states = []
score = 0

def show_result():
    titoo = turtle.Turtle()
    titoo.hideturtle()
    titoo.color("red")
    titoo.write(f"Good Job. Your score is : {len(guessed_states)}/36.",align="center", font=("Impact", 65, "normal"))
    titoo.goto(0,0)

while len(guessed_states) < 36:
    answer = screen.textinput(title=f"{len(guessed_states)}/36 guessed", prompt="Write a state's name:")
    if answer == "exit":
        states_to_learn = [state for state in states
            if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data =data[data.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.color("#AAFF00")
        t.write(f"{answer}",align="center", font=("Impact", 16, "normal"))

show_result()

screen.exitonclick()


