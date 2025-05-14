# moveturtle.py
# Controls the player turtle's movement in the turtle crossing game

from turtle import *

class MoveT:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.color("white")              # Set turtle color
        self.turtle.shape("turtle")             # Use the turtle shape
        self.turtle.penup()                     # Prevent drawing lines
        self.turtle.goto(0, -275)               # Start at the bottom center of the screen
        self.turtle.setheading(90)              # Point upwards

    def move(self):
        """Moves the turtle forward (up)."""
        self.turtle.fd(10)

    def back(self):
        """Moves the turtle backward (down)."""
        self.turtle.backward(10)
