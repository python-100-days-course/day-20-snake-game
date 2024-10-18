# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 21 - Intermediate - Build the Snake Game Part 2: Class Inheritance & Slicing List and Dictionaries
# Not used in the game, was created to learn new concepts.

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this under water.")

    def swim(self):
        print("Moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)