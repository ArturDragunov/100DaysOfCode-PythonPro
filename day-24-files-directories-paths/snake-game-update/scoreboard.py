from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')
FILE_PATH = 'day-20-21-snake-game\data.txt'
class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.read_high_score()
    self.color('white')
    self.penup()
    self.goto(x = 0, y = 270)
    self.hideturtle()
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f'Score: {self.score} High Score: {self.high_score}',  align=ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      self.write_high_score()
    self.score = 0
    self.update_scoreboard()

  def write_high_score(self):
    with open(FILE_PATH, mode='w') as file:
      file.write(str(self.high_score))

  # def game_over(self):
  #   self.goto(0,0)
  #   self.write('GAME OVER',  align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score +=1
    self.clear()
    self.update_scoreboard()

  def read_high_score(self):
    with open(FILE_PATH, mode='r') as file:
      self.high_score = int(file.read())
