from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.setpos(0, 0)
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.1

    def move(self):
        if self.ycor() >= 300 or self.ycor() <= -300:
            self.y_move *= -1

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1
        self.move_speed /= 1.5

    def next_round(self):
        self.goto(0, 0)
        self.bounce()
        self.move_speed = 0.1
