# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates
# Day 21 - Intermediate - Build the Snake Game Part 2: Class Inheritance & Slicing List and Dictionaries
# Not used in the game, old code.

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn off turtle animation

# Everything related to turtle/snake was moved to snake.py
starting_positions = [(0, 0), (-20, 0), (-40, 0)] # list of tuples with x and y coordinates

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # adds 0.1 second delay

    # each segment takes the position of the previous segment, starting from last segment
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()