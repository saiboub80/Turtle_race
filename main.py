from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='which turtle will win the race? Enter a color:  ')
color=['red','orange','blue', 'green', 'yellow', 'purple']
y_positions = [-70,-40,-10,20,50,80]
all_turtles =[]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet :
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                '''The winner will be show on the screen'''
                screen.title(f"you've won! The {winner_color} turtl is the winner")
            else:
                '''The loser will be show on the top of the screen'''
                screen.title(f"you've lost! The {winner_color} turtl is the winner")
        ran_distance =random.randint(0,10)
        turtle.forward(ran_distance)


screen.exitonclick()