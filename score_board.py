# score_board.py
# Handles score display, level-up message, game over text, and start countdown

import time
from turtle import *

class score:
    def __init__(self):
        # Turtle objects for various UI texts
        self.tim = Turtle()    # Displays the "Level=" label
        self.tun = Turtle()    # Displays the current level value
        self.tung = Turtle()   # Displays "GAME OVER!" message
        self.popup = Turtle()  # Displays "LEVEL UP!" message

    def scoreboard(self, sore):
        """Displays the current level on the screen."""
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.color("white")
        self.tim.goto(-425, 265)
        self.tim.write("Level= ", align="center", font=("Courier", 12, "normal"))
        
        self.tun.penup()
        self.tun.hideturtle()
        self.tun.color("white")
        self.tun.goto(-375, 265)
        self.tun.clear()  # Clear previous level text
        self.tun.write(sore, align="right", font=("Courier", 12, "normal"))

    def game_over(self):
        """Displays 'GAME OVER!' at the center of the screen."""
        self.tung.penup()
        self.tung.hideturtle()
        self.tung.color("white")
        self.tung.goto(0, 0)
        self.tung.clear()
        self.tung.write("GAME OVER!", align="right", font=("Courier", 12, "bold"))

    def level_up(self):
        """Displays a temporary 'LEVEL UP!' message."""
        self.popup = Turtle()
        self.popup.hideturtle()
        self.popup.penup()
        self.popup.color("white")
        self.popup.goto(0, 0)
        self.popup.write("LEVEL UP!", align="center", font=("Courier", 12, "bold"))

    def ready(self):
        """Shows the starting message and a 3-second countdown."""
        self.countdown = Turtle()
        self.countdown.hideturtle()
        self.countdown.penup()
        self.countdown.color("white")
        self.countdown.goto(0, 0)
        self.countdown.write(
            "You have to Help the turtle to cross the road\n                 Get Ready!",
            align="center",
            font=("Courier", 12, "bold")
        )
        Screen().update()
        time.sleep(1)
        self.countdown.clear()

        # Countdown from 3 to 1
        for i in range(3, 0, -1):
            self.countdown.clear()
            self.countdown.write(i, align="center", font=("Courier", 18, "bold"))
            time.sleep(1)
            Screen().update()
        
        self.countdown.clear()
        Screen().update()
