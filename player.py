from turtle import Turtle

## Constants ##

# Turtle size
WIDTH = 1.2
HEIGHT = 1.2   # All turtles start out as 20 x 20

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("White")
        self.goto(STARTING_POSITION)
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)
        self.color("Black")
        self.left(90) # Turtle facing up


    def go_up(self):
        new_up = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_up)

    def go_back(self):
        new_up = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_up)
