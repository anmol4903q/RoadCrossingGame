# car_gen.py
# Handles car creation and movement in the turtle crossing game

from turtle import *
import random

class Car:
    def __init__(self):
        self.all_cars = []  # Stores all car objects currently on screen

    def spawn(self, level):
        """
        Spawns a new car at a random y-position from the left side based on level difficulty.
        Higher levels increase spawn frequency.
        """
        spawn_chance = max(9 - level, 1)  # Cars spawn more frequently as level increases

        if random.randint(1, spawn_chance) == 1:
            colours = ["red", "yellow", "DeepSkyBlue", "orange", "grey", "magenta", "blue", "purple"]
            self.car = Turtle()
            self.car.shape("square")
            self.car.shapesize(stretch_wid=1, stretch_len=2)  # Make the car rectangle-shaped
            self.car.color(random.choice(colours))            # Random car color
            self.car.penup()
            yaxis = random.randint(-240, 240)                 # Random vertical position
            self.car.goto(-550, yaxis)                        # Start from the left off-screen
            self.car.fd(10)                                   # Move a bit into view
            self.all_cars.append(self.car)                    # Add to list of active cars

    def car_move(self, speed):
        """
        Moves all active cars forward based on current speed.
        """
        for cars in self.all_cars:
            cars.fd(speed)
