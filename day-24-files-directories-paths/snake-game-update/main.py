from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()

screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0) # screen is frozen. You don't see animation

snake=Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up,'Up') # when adding a function into a function, don't use ()
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(0.1) # delay after all 3 segments are moved
  snake.move()

  # detect collision with food
  if snake.head.distance(food) < 15: # first instance of the snake. food is r=10, so if r<15, then they collided
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  # Detect collision with wall.
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()
  # Detect collision with tail.
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10: # if any part of the body has short distance (each square is 20x20)
      # so distance <10 assumes that you go into the pixels of the body
      scoreboard.reset()
      snake.reset()

screen.exitonclick()