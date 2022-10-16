from turtle import Screen
# from lines import Lines
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")

screen.tracer(0)
line = Line()
screen.listen()

pr = Paddle(350)
screen.onkey(pr.paddle_up, "Up")
screen.onkey(pr.paddle_down, "Down")

pl = Paddle(-350)
screen.onkey(pl.paddle_up, "w")
screen.onkey(pl.paddle_down, "s")


score_left = Scoreboard(1, -150)
score_right = Scoreboard(2, 150)

ball = Ball()

screen.update()
game_is_on = True

while game_is_on:
    ball.move()

    # collision witch paddle
    if pr.xcor()-20 == ball.xcor() and pr.ycor() + 60 > ball.ycor() > pr.ycor() - 60:
        ball.bounce()

    if pl.xcor()+20 == ball.xcor() and pl.ycor() + 60 > ball.ycor() > pl.ycor() - 60:
        ball.bounce()

    if ball.xcor() > pr.xcor():
        ball.next_round()
        score_left.add_score()

    if ball.xcor() < pl.xcor():
        ball.next_round()
        score_right.add_score()

    if score_right.score == 10:
        score_right.winner()
        game_is_on = False
    elif score_left.score == 10:
        score_left.winner()
        game_is_on = False

    screen.update()
    time.sleep(ball.move_speed)

screen.exitonclick()
