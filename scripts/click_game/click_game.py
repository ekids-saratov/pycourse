from turtle import Screen, Turtle
import random
import time

gift_box_shapes = ["gift_box1.gif", "gift_box2.gif", "gift_box3.gif"]

wn_width = 300
wn_height = 300

wn = Screen()
wn.screensize(wn_width, wn_height)
wn.register_shape(gift_box_shapes[0])
wn.register_shape(gift_box_shapes[1])
wn.register_shape(gift_box_shapes[2])
wn.bgcolor("pink")

# score
score_value = 0

score = Turtle()
score.hideturtle()
score.penup()
score.color("white")
score.goto(-290, 290)
score.write("score: " + str(score_value), font=("Arial", 26, "normal"))


# gift 1
shape_id = random.randint(0,2)  
box1_pos = random.randint(-200,200)
gift_box1 = Turtle(shape=gift_box_shapes[shape_id], visible=False)
gift_box1.left(90)
gift_box1.penup()



def init_box():
    shape_id = random.randint(0,2)
    gift_box1.shape(gift_box_shapes[shape_id])
    box1_pos = random.randint(-200,200)
    gift_box1.goto(box1_pos, 200)

    box1_speed =  random.randint(0,10)
    gift_box1.speed(box1_speed)
    gift_box1.onclick(box_click, 1)
    gift_box1.showturtle()


def box_click(x,y):
    global score_value
    score_value += 1
    gift_box1.hideturtle()
    score.clear()
    score.write("score: " + str(score_value), font=("Arial", 26, "normal"))
    init_box()

init_box()

# main loop
while gift_box1.ycor() > -260:
    gift_box1.backward(10)
    print(str(gift_box1.ycor()))
    if gift_box1.ycor() < -250:        
        gift_box1.hideturtle()
        init_box()
    time.sleep(1/50)


wn.mainloop()
print('ok')
