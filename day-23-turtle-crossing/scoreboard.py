from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color('black')
    self.penup()
    self.hideturtle()
    self.score = 0
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-220,250)
    self.write(f"Level: {self.score}", align='center', font=FONT)

  def score_increase(self):
    self.score +=1
    self.update_scoreboard()

  def game_over(self):
    self.goto(0,0)
    self.write('GAME OVER',  align='center', font=FONT)
