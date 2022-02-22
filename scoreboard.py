from turtle import Turtle

WIDTH = 800
HEIGHT = 600
ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    """Class for creating, writing and updating the scoreboard. Extends Turtle"""
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear scoreboard, rewrite new scores"""
        self.clear()
        self.goto(-100,200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
    
    def right_point(self):
        """Increase the points for right side"""
        self.right_score += 1
        self.update_scoreboard()
    
    def left_point(self):
        """"increase the points for left side"""
        self.left_score += 1
        self.update_scoreboard()