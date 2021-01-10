from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["pink", "blue", "green", "purple", "red", "orange"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range (0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




# ping = Turtle(shape="turtle")
# ping.color("blue")
# ping.penup()
# ping.goto(x=-230, y=-50)
#
# reed = Turtle(shape="turtle")
# reed.color("green")
# reed.penup()
# reed.goto(x=-230, y=0)
#
# cam = Turtle(shape="turtle")
# cam.color("purple")
# cam.penup()
# cam.goto(x=-230, y=50)
#
# jay = Turtle(shape="turtle")
# jay.color("red")
# jay.penup()
# jay.goto(x=-230, y=100)
#
# fifi = Turtle(shape="turtle")
# fifi.color("orange")
# fifi.penup()
# fifi.goto(x=-230, y=150)



screen.exitonclick()

