from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.up()
        self.shapesize(1, 5)
        self.goto(position_x, 0)

    def paddle_up(self):
        if self.ycor() + 50 < 300:
            self.forward(20)

    def paddle_down(self):
        if self.ycor() - 50 > -300:
            self.backward(20)
