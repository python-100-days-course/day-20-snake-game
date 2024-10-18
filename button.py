# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates
# Day 21 - Intermediate - Build the Snake Game Part 2: Class Inheritance & Slicing List and Dictionaries
# Test file to use on screen buttons to control the snake on a phone, instead of the keyboard

# Note: not working, yet

from turtle import Screen, Turtle
from functools import partial

CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'normal')

class Button(Turtle):
    def __init__(self, text, location, onclick_action):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.fillcolor('blue')
        self.penup()
        self.goto(location)
        self.write(text, align='center', font=FONT)
        self.sety(150 + CURSOR_SIZE + FONT_SIZE)
        self.onclick(partial(onclick_action, "x"))
        self.showturtle()

# turtle = Turtle()
# turtle.hideturtle()
#
# screen = Screen()
# screen.mainloop()
#
#
#
#
#
#
#
#
#
#
#
# # Referance code
# # Source: https://stackoverflow.com/questions/59902849/how-can-i-create-a-button-in-turtle
# from turtle import Screen, Turtle
#
# CURSOR_SIZE = 20
# FONT_SIZE = 12
# FONT = ('Arial', FONT_SIZE, 'bold')
#
# def draw_onclick(x, y):
#     turtle.dot(100, 'cyan')
#
# button = Turtle()
# button.hideturtle()
# button.shape('circle')
# button.fillcolor('red')
# button.penup()
# button.goto(150, 150)
# button.write("Click me!", align='center', font=FONT)
# button.sety(150 + CURSOR_SIZE + FONT_SIZE)
# button.onclick(draw_onclick)
# button.showturtle()
#
# turtle = Turtle()
# turtle.hideturtle()
#
# screen = Screen()
# screen.mainloop()