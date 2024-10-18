from turtle import Turtle

ALIGNMENT = "left"
ALIGNMENT_2 = "center"
FONT = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.goto(x=-30, y=270)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.display()

    def display(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", False, align=ALIGNMENT_2, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.display()