import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
fred = turtle.Turtle('triangle')


sc = turtle.Screen()
sc.reset()
sc.colormode(1.0)

fred.pensize(width=10)
fred.turtlesize(3)

print((fred.xcor(),fred.ycor()))
fred.penup()
# sc.setworldcoordinates(0,-1.5,360,1.5)

# for angle in range(360):
#     y = math.sin(math.radians(angle))
#     fred.goto(angle,y)  

radius = 5
step = 5


fred.color('black')
for angle in range(0, 720, step):
    x = math.cos(math.radians(angle)) * radius
    y = math.sin(math.radians(angle)) * radius
    
    if (fred.xcor() != 0.0):
    	fred.pendown()
    fred.setheading(angle  + 90)
    fred.goto(x,y)
    radius += 1
    r = ((angle / 720 ) / 3) % 86
    g = (2 * (angle /  720 )  / 3 )% 172
    b = (angle / 720 ) % 255
    print({'r':r, 'g':g, 'b':b,'radius':radius,'num':angle/step,'x':x,'y':y})  

    fred.color((r,g,b))

wn.exitonclick()

