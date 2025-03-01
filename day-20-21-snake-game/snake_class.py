from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]  # Corrected order of positions
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
  def __init__(self): # init is constructor. Is automatically called when an instance is created
    self.segments=[]
    self.starter() # when object created, we initialize attributes of the object with self.starter()
    self.head = self.segments[0]
  def starter(self):
    for position in positions:
      self.add_segment(position)

  def add_segment(self, position):
      snake = Turtle(shape='square')
      snake.color('white')
      snake.penup()
      snake.goto(position)
      self.segments.append(snake)

  def extend(self):
    self.add_segment(self.segments[-1].position()) # we are adding a new part into the last position of the body.
# then it will start moving from the previous [-1] position. (so, at the start, there are two boxes sharing same pixels)
  def move(self):
    for seg_num in range(len(self.segments)-1,0,-1): # range(start = len(segments)-1,stop = 0,step = -1)
      new_x = self.segments[seg_num-1].xcor()
      new_y = self.segments[seg_num-1].ycor()
      self.segments[seg_num].goto(new_x,new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN: # (we can't go over the head) 
      self.head.setheading(UP)
  def down(self):
    if self.head.heading() != UP: # (we can't go over the head) 
      self.head.setheading(DOWN)    
  def right(self):
    if self.head.heading() != LEFT: # (we can't go over the head) 
      self.head.setheading(RIGHT)    
  def left(self):
    if self.head.heading() != RIGHT: # (we can't go over the head) 
      self.head.setheading(LEFT)    
