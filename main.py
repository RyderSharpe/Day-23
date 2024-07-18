import time
from turtle import Screen
from player import Player
from car_manager import CarManager

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)  # Turn off automatic screen updates

# Initialize game elements after screen setup
turt = Player()
cars = CarManager()

# Controls
screen.listen()
screen.onkey(turt.go_up, "Up")
screen.onkey(turt.go_back, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Code will refresh every 0.1 seconds
    screen.update()
