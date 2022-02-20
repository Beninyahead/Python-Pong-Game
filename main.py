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

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

# Screen listener functions
screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_is_on = True
# Basic game loop, refresh every 0.1 second
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    ball.detect_wall_collision()
    ball.detect_paddle_collision(r_paddle,l_paddle)
    ball.detect_goal(score)

screen.exitonclick()