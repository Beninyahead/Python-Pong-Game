from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.MOVESIZE = 20
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        #self.setheading(90)
        self.color('white')
        #self.speed(0)
        self.goto(position)
    
    def up(self):
        if self.ycor() < 250:
            new_y = self.ycor() +20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() -20
            self.goto(self.xcor(),new_y)
    