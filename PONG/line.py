from turtle import Turtle


class Line(Turtle):

    def __init__(self):

        super().__init__()
        self.shape("square")
        self.penup()
        for pos in range(285, -300, -60):
            self.goto(x=0, y=pos)
            self.pendown()
            self.width(3)
            self.hideturtle()
            self.color("white")
            self.goto(x=0, y=pos-30)
            self.penup()
