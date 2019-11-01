import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
fred = turtle.Turtle('turtle')
fred.color('red')
sc = turtle.Screen()
sc.reset()

print((fred.xcor(),fred.ycor()))
fred.penup()
# sc.setworldcoordinates(0,-1.5,360,1.5)

# for angle in range(360):
#     y = math.sin(math.radians(angle))
#     fred.goto(angle,y)  

scale = 100

fred.color('purple')
for angle in range(-180,180):
    x = math.cos(math.radians(angle)) * scale
    y = math.sin(math.radians(angle)) * scale
    print((angle,x,y))  
    if (fred.xcor() != 0.0):
    	fred.pendown()
    fred.setheading(angle  + 90)
    fred.goto(x,y)

wn.exitonclick()

