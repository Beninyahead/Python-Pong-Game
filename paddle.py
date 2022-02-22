from turtle import Turtle

class Paddle(Turtle):
    """Class for creating and moving the paddle, Extends Turtle"""
    def __init__(self, position) -> None:
        super().__init__()
        self.MOVESIZE = 20
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color('white')
        self.goto(position)
    
    def up(self):
        """Move the paddle up"""
        if self.ycor() < 250:
            new_y = self.ycor() +self.MOVESIZE
            self.goto(self.xcor(), new_y)

    def down(self):
        """Move the paddle down"""
        if self.ycor() > -240:
            new_y = self.ycor() -self.MOVESIZE
            self.goto(self.xcor(),new_y)
    