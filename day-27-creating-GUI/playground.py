# * represents unlimited amount of arguments. Unlimited Positional Arguments (5,4,3)
def add(*args):
  total_sum = 0
  for n in args: # args is a tuple
    total_sum+=n
  return total_sum

add(5,4,3)

# ** defines unlimited amount of keyword arguments. We get a dictionary {'add': 3, 'multiply': 5}
def calculate(n,**kwargs):
  print(kwargs) # kwargs is a dictionary
  n += kwargs['add']
  n *= kwargs['multiply']
  print(n)

calculate(2,add=3, multiply=5)

class Car:
  def __init__(self, **kw):
    self.make = kw['make']
    self.model = kw.get('model') # if model wasn't provided, it's set to None
    self.color = kw.get('color')
    self.seats = kw.get('seats')

# my_car = Car(make='Nissan', model='GT-R')
my_car = Car(make='Nissan')
print(my_car.make)
print(my_car.model) # None

def all_aboard(a, *args, **kwargs): # 4 (7, 3, 0) {'x': 10, 'y': 64}
  print(a,args,kwargs)
all_aboard(4,7,3,0,x=10,y=64)