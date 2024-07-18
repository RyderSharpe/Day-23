COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Car size
HEIGHT = 1
LENGTH = 3

RANDOM_Y = list(range(-300, 301))


from turtle import Turtle
import random

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("Black")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=LENGTH)
        self.goto(320,0)
