from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
  def __init__(self):
    self.all_cars = []
    self.level = 0
    self.move_speed = STARTING_MOVE_DISTANCE
  
  def create_car(self):
    if random.uniform(0,1) > 0.7: # 10% chance to generate a car for each run
      new_car = Turtle('square')
      new_car.penup()
      new_car.shapesize(stretch_len=2,stretch_wid=1) # we change 20x20 pixel size of a turtle into a smaller dot
      new_car.color(random.choice(COLORS))
      new_car.goto(x=300,y=random.randint(-250,250))
      self.all_cars.append(new_car)
  def move(self):
    for car in self.all_cars:
      car.backward(self.move_speed)
  def update_speed(self):
    self.level += 1
    self.move_speed += MOVE_INCREMENT*self.level
  def delete_car(self):
    for car in self.all_cars:
      if car.xcor() < -300:
        car.hideturtle()  # Hide the turtle
        self.all_cars.remove(car)  # Remove from the list
        del car
