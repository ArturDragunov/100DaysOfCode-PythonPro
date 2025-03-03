import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score_board = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkey(player.go_up,'Up')

game_is_on = True
while game_is_on:
  cars.create_car()
  cars.move()
  time.sleep(0.1)
  screen.update()
# Detect collision with top-edge
  if player.ycor() > 280:
    player.reset_position()
    score_board.score_increase()
    cars.level = score_board.score
    cars.update_speed()

# Detect collision with car
  for car in cars.all_cars:
    if car.distance(player) < 30:
      game_is_on = False
      score_board.game_over()

# Delete car when it reaches end of screen to save memory
  cars.delete_car()


screen.exitonclick()
