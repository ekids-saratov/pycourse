# ping pong game using out of the box libraries
import time
import turtle
import sys
 

window = turtle.Screen()
window.title("Ping pong python game")
window.bgcolor("#451261")
window.setup(width=800, height=600)
window.tracer(0)  # stops window from repainting. it will speed up game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of repaining
paddle_a.shape("square")  # square cyrcle triangle
paddle_a.color("#c499f3")
paddle_a.penup()  # do not drow line while moving
paddle_a.goto(-350, 0)
# default size 20px x 20 px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of repaining
paddle_b.shape("square")  # square cyrcle triangle # Ball
paddle_b.color("#c499f3")
paddle_b.penup()  # do not drow line while moving
paddle_b.goto(350, 0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")  # square cyrcle triangle # Ball
ball.color("#c499f3")
ball.penup()  # do not drow line while moving
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
# tells the program to listen to the keybard input
window.listen()
# bind  key press on "w" key on keyboard to invocation of puddle_a_up() function
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")


#beep sound
def beep():
    sys.stdout.write('\r\a{1}')
    sys.stdout.flush()

# Main game loop
while(True):
    window.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        beep()
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        beep()

    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1


     # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        beep()
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        beep()


    time.sleep(1/75) # screen refresh speed

    
