from turtle import Turtle
import random

WIDTH = 800
HEIGHT = 600
START_SPEED = 0.1

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.y_trajectory = 10
        self.x_trajectory = 10
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color('white')
        self.move_speed = START_SPEED

    def move(self):
        new_x = self.xcor() + self.x_trajectory
        new_y = self.ycor() + self.y_trajectory
        self.goto(new_x,new_y)

    def detect_wall_collision(self):
        if self.ycor() >= HEIGHT/2 - 15 or self.ycor() <= HEIGHT/-2 + 15:
            self.y_trajectory *= -1
    
    def detect_paddle_collision(self, r_paddle, l_paddle):
        if ((self.distance(r_paddle) < 50 and self.xcor() > WIDTH/2 -60)
            or (self.distance(l_paddle) < 50 and self.xcor() < WIDTH/-2 +60) ):
            self.x_trajectory *= -1
            self.move_speed *= 0.9
        
    def detect_goal(self,score):
        if self.xcor() > WIDTH/2 -20:
            print("Left player scored a goal")
            score.l_point()
            self.goto(0,0)
            self.move_speed = START_SPEED
            self.x_trajectory *=-1
        if self.xcor() < WIDTH/-2 +20:
            print("Right player scored a goal")
            score.r_point()
            self.goto(0,0)
            self.move_speed = START_SPEED
            self.x_trajectory *=-1