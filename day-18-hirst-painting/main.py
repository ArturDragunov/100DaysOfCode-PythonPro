from turtle import Turtle, Screen
import turtle as t
from random import choice

# import colorgram

# colors = colorgram.extract('day-18-hirst-painting\image.jpg',90)
# rgb_tuples = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# print(rgb_tuples)

color_list = [(242, 248, 246), (201, 172, 110), (154, 180, 195), (193, 162, 177), (153, 186, 174), (214, 203, 117), (208, 179, 196), (175, 189, 212), (161, 212, 186), (163, 202, 213), (192, 163, 57), (114, 122, 184), (214, 181, 180), (198, 206, 47)]
t.colormode(255)
tim = Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
  tim.dot(20, choice(color_list))
  tim.forward(50)

  if dot_count % 10 == 0:
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = Screen()
screen.exitonclick()