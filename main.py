from myFunctions import *
#Name: Vortexes
turtle.tracer(0)
#bob.speed(0)


jump(0,-1000)
bob.fillcolor('black')
bob.begin_fill()
bob.circle(1000)
bob.end_fill()

jump(0,-175)
bob.fillcolor('white')
bob.begin_fill()
bob.circle(175)
bob.end_fill()

jump(0,0)
for times in range( 256 ):
    c = ( times, 0, 255 )
    bob.color(c)
    bob.forward(times * 2)
    bob.left(91)
jump(0,0)
    
    
for times in range(50):
    polygon(3,10,c)
    bob.left(36)
    
jump(-400,300)

for times in range( 256 ):
    c = (0, times, 255 )
    bob.color(c)
    bob.forward(times * 2)
    bob.left(91)
    
jump(400,300)

for times in range( 256 ):
    c = (0, 255, times )
    bob.color(c)
    bob.forward(times * 2)
    bob.left(91)

jump(400,-300)
for times in range( 256 ):
    c = (255, times, 0 )
    bob.color(c)
    bob.forward(times * 2)
    bob.left(91)

jump(-400,-300)

for times in range( 256 ):
    c = (times, 255,times )
    bob.color(c)
    bob.forward(times * 2)
    bob.left(91)







       


