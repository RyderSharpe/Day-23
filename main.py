import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)  # Turn off automatic screen updates

CAR_X = 300
CAR_Y = random.randrange(-300, 301)
DIFFICULTY = 6
MIN_DIFFICULTY = 1

# Initialize game elements after screen setup
turt = Player()
score = Scoreboard()
cars = CarManager(CAR_X, CAR_Y, DIFFICULTY)  # Pass parameters here

# Controls
screen.listen()
screen.onkey(turt.go_up, "Up")
screen.onkey(turt.go_back, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Code will refresh every 0.1 seconds
    screen.update()
    cars.moving()
    cars.create_new_car()

    for car in cars.all_cars:
        if turt.distance(car) < 30: # and turt.xcor() > 340 or turt.distance(car) < 40 and turt.xcor() < -340:
            print("Game Over")
            game_is_on = False
            score.game_over()

    if turt.ycor() > 280:  # Example height for difficulty increase
        score.increase_score()
        score.update_score()
        cars.car_speed += 5  # Increase car speed
        turt.goto(0, -280)  # Reset turtle position
        DIFFICULTY = max(MIN_DIFFICULTY, DIFFICULTY - 1)  # Decrease difficulty but not below 1
        print(DIFFICULTY)

screen.exitonclick()
