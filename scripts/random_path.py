
import turtle, random


def step():
    R = random.randrange(0,257,5)
    G = random.randrange(0,257,5)
    B = random.randrange(0,257,5)
    turtle.color(R,G,B)
    # turtle.setheading(random.randrange(360))
    turtle.right(random.randrange(90))
    turtle.forward(random.randrange(5,50))

turtle.shape('turtle')
turtle.colormode(255)
turtle.pensize(5)

def qt():
	turtle.bye()

turtle.listen()
for i in range(1000):
    step()
    turtle.onkey(qt, 'space')

    





