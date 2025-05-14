# Turtle_crossing (main.py)
from turtle import *
import time
from moveturtle import MoveT
from car_gen import Car
from score_board import score

# Setup screen and drawing turtle
tim = Turtle()
screen = Screen()
screen.tracer(0)  # Disable automatic screen updates for smoother animation
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("ROAD CROSSING")
tim.speed("fastest")
tim.color("DarkGreen")
tim.hideturtle()

# Draw upper footpath
tim.penup()
tim.goto(x=-300, y=250)
tim.pendown()
tim.goto(x=-500, y=275)
tim.pensize(50)
tim.fd(1000)

# Draw lower footpath
tim.penup()
tim.goto(x=300, y=-250)
tim.goto(x=500, y=-275)
tim.pendown()
tim.backward(1000)

# Create player, cars, and scoreboard objects
move = MoveT()
car = Car()
score = score()

# Draw road lines in the middle
tim.color("white")
tim.pensize(5)
xpos = -500
ypos = [-150, -50, 50, 150]
for y in ypos:
    for i in range(30):
        tim.speed("fastest")
        tim.penup()
        tim.goto(xpos + i * 50, y)
        tim.pendown()
        tim.fd(20)

# Game variables
level = 1
speed = 5

# Setup key controls
screen.listen()
screen.onkey(move.move, "Up")
screen.onkey(move.back, "Down")

# Show intro countdown
score.ready()

# Start game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)  # Control overall game speed

    car.spawn(level)      # Try to spawn a car
    car.car_move(speed)   # Move all cars

    # Detect collision with any car
    for carss in car.all_cars:
        if carss.distance(move.turtle) < 22:
            game_on = False

    # Detect if turtle reaches the goal (top)
    yco = move.turtle.ycor()
    if yco > 280:
        move.turtle.goto(0, -275)  # Reset turtle to start
        move.turtle.setheading(90)
        level += 1                 # Increase level
        speed += 3                 # Increase car speed
        speed = min(speed, 20)     # Cap speed to avoid too fast cars

        score.level_up()           # Show level up message
        screen.update()
        time.sleep(1)
        score.popup.clear()

        # Clear all old cars
        for c in car.all_cars:
            c.hideturtle()
        car.all_cars.clear()

    # Update score on screen
    score.scoreboard(level)

# Game over message
if not game_on:
    score.game_over()

exitonclick()  # Close game on click
