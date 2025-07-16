import turtle
#turtle.shape("turtle")  # optional
#turtle.speed(0)         # optional
#turtle.forward(90)
#turtle.left(90)
#turtle.forward(90)
#turtle.left(90)
#turtle.forward(90)
#turtle.left(90)
#turtle.forward(90)

#turtle.Screen().exitonclick()
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()