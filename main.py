from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title="make your bet", prompt="which turtle will win the race?Choose the color from this (Red, Orange, Green, Yellow, Blue, Purple):") 
colors= ["red", "orange", "green", "yellow", "blue", "purple"]
race_on = False
turtles = []
a=[20,60,100,-20,-60,-100]

for turtle_pos in range(0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_pos])
    tim.goto(x=-230, y=a[turtle_pos])
    turtles.append(tim)
if user_bet:
    race_on = True
while race_on:
    for turtle in turtles:
        if turtle.xcor()>240:
            race_on= False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")

        distance = random.randint(0,10)
        turtle.forward(distance)












screen.exitonclick()
