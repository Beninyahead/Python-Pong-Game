from turtle import Turtle

from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
START_SPEED = 0.1

class Ball(Turtle):
    """Class for creating and moving the ball. Extends Turtle"""
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
        """Move the ball forward by x and y trajectories"""
        new_x = self.xcor() + self.x_trajectory
        new_y = self.ycor() + self.y_trajectory
        self.goto(new_x,new_y)

    def detect_wall_collision(self):
        """Detect a wall colision, reverse y trajectory to "bounce" the ball"""
        if self.ycor() >= HEIGHT/2 - 15 or self.ycor() <= HEIGHT/-2 + 15:
            self.y_trajectory *= -1
    
    def detect_paddle_collision(self, r_paddle, l_paddle):
        """Detect a collision with the paddles
        If collision, reverse x trajectory"""
        if ((self.distance(r_paddle) < 50 and self.xcor() > WIDTH/2 -60)
            or (self.distance(l_paddle) < 50 and self.xcor() < WIDTH/-2 +60) ):
            self.x_trajectory *= -1
            self.move_speed *= 0.9
        
    def detect_goal(self,score:Scoreboard):
        """Detect a collision with walls. If collision, then goal.
        Reset ball to startign values, move in opposite of previous x trajectory """
        
        if self.xcor() > WIDTH/2 -20:
            print("Left player scored a goal")
            score.left_point()
            self.goto(0,0)
            self.move_speed = START_SPEED
            self.x_trajectory *=-1

        if self.xcor() < WIDTH/-2 +20:
            print("Right player scored a goal")
            score.right_point()
            self.goto(0,0)
            self.move_speed = START_SPEED
            self.x_trajectory *=-1