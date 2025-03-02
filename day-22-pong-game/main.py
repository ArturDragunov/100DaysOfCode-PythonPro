from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width = 800, height = 600)
screen.bgcolor('black')
screen.title('Ping Pong Game')
screen.tracer(0) # screen is frozen. You don't see animation

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,'Up') # when adding a function into a function, don't use ()
screen.onkey(r_paddle.go_down,'Down')
screen.onkey(l_paddle.go_up,'w') # when adding a function into a function, don't use ()
screen.onkey(l_paddle.go_down,'s')

game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  # Detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280: # upper part of the wall
    # needs to bounce
    ball.bounce_y()

  # Detect collision with r_paddle
  # we need second condition because we can't measure distance to the edge of paddle
  if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320): 
    ball.bounce_x()

# went out of r_paddle
  if ball.xcor() > 380: 
    ball.reset_position()
    scoreboard.l_point()

# went out of l_paddle
  if ball.xcor() < -380: 
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()
