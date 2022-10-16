from turtle import Turtle
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self, number, pos_x):
        super().__init__()
        self.number = number
        self.score = 0
        self.color("white")
        self.up()
        self.hideturtle()
        self.goto(x=pos_x, y=250)
        self.write(f"Player {self.number} score: {self.score}", False, 'center', FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Player {self.number} score: {self.score}", False, 'center', FONT)

    def game_over(self):
        if self.score >= 10:
            return True
        else:
            return False

    def winner(self):
        self.penup()
        self.goto(0, 30)
        self.write(f"THE WINNER IS PLAYER {self.number}", False, 'center', FONT)
