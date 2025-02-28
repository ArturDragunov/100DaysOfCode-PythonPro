from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color:')
colors = ['red','orange','yellow','green','blue','purple']

starting_x = -230
starting_y = -70
turtles = []
for i in range(6):
  tim = Turtle(shape='turtle')
  tim.penup()
  tim.goto(x=starting_x,y=starting_y+i*30)
  tim.color(colors[i])
  turtles.append(tim)
  
if user_bet:
  is_race_on=True

while is_race_on:
  for turtle in turtles:
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)
    if turtle.xcor()>230:
      is_race_on=False
      if user_bet==turtle.pencolor():
        print(f'You won! First turtle to come was {turtle.pencolor()}')
      else:
        print(f'You lost. First turtle to come was {turtle.pencolor()}')

screen.exitonclick()