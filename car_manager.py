from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Car size
WIDTH = 1
LENGTH = 2

RANDOM_COLOR = random.choice(COLORS)

CAR_X = 300
CAR_Y = random.randrange(-300, 301)


class CarManager():

    def __init__(self, car_x, car_y, difficulty):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_x = car_x  # Store the passed car_x value
        self.car_y = car_y  # Store the passed car_y value
        self.difficulty = difficulty  # Store the passed difficulty value

    def create_new_car(self):
        chance = random.randint(1, self.difficulty)  # frequency of cars based on difficulty
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def moving(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
