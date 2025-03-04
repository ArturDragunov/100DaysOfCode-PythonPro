from turtle import Turtle
import random
class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.penup()
    self.shapesize(stretch_len=0.5,stretch_wid=0.5) # we change 20x20 pixel size of a turtle into a smaller dot
    self.color('blue')
    self.speed('fastest')
    self.refresh() # we set up initial location with initialization

  def refresh(self): # and then each time we collide we also refresh the location
    random_x = random.randint(-280,280) # X axis is in range [-300,300]
    random_y = random.randint(-280,280)
    self.goto(random_x, random_y)    