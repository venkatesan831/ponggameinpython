import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)



l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
t = 0.100
is_on = True
while is_on:
    time.sleep(t)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        scoreboard.increase_rscore()
        t -= 0.001

    elif ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        scoreboard.increase_lscore()
        t -= 0.001

    if ball.xcor() > 400:
        ball.setposition(0, 0)
        ball.bounce_x()
        scoreboard.increase_lscore()
    elif ball.xcor() < -400:
        ball.setposition(0, 0)
        ball.bounce_x()
        scoreboard.increase_rscore()





screen.exitonclick()



