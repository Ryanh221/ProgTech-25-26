import turtle
bob = turtle.Turtle()
turtle.colormode(255)

# Sun design
def sun1(x,y):
  jump(x,y)
  bob.pensize(10)
  for times in range(10):
    polygon(3,20)
    bob.forward(30)
    bob.left(36)
  jump(16 + x,-75 + y)

def polygon(sides, dist, color):
  angle = 360/sides
  bob.fillcolor(color)
  bob.begin_fill()
  for times in range(sides):        
    bob.forward(dist)
    bob.left(angle)
  bob.end_fill()


def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
  
def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times)
    bob.forward(distance)
    bob.left(angle)

def home():
  bob.penup()
  bob.home()
  bob.pendown()


def plus(c,distance):
  bob.color(c)
  for times in range(4):
    bob.forward(distance)
    bob.left(90)
    bob.forward(distance)
    bob.right(90)
    bob.forward(distance)
    bob.left(90)
    
    
