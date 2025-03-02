from turtle import Turtle
class Paddle(Turtle):
  def __init__(self,coordinates):
    super().__init__()
    self.shape('square')
    self.penup()
    self.shapesize(stretch_len=1,stretch_wid=5) # we change 20x20 pixel size of a turtle into a smaller dot
    self.color('white')
    self.speed('fastest')
    self.goto(coordinates)

  def go_up(self):
    new_y = self.ycor()+ 20
    self.goto(self.xcor(),new_y)

  def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(),new_y)