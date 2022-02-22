from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20

# Screen:
screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((360,0))
left_paddle = Paddle((-360,0))
ball = Ball()
scoreboard = Scoreboard()

# Screen listener functions
screen.listen()
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')
screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')

game_is_on = True
# Basic game loop, refresh every 0.1 second
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    ball.detect_wall_collision()
    ball.detect_paddle_collision(right_paddle,left_paddle)
    ball.detect_goal(scoreboard)

screen.exitonclick()