import random
import time
import turtle

# Конфигурируем экран программы, задаем начальные свойства
window = turtle.Screen()  # Создаем экземпляр класса (объект) Screen и прискаеваем его в переменную window
window.title('Snake Game')  # Задаем заголовок окна
window.bgcolor('#8b1c71')  # Задаем цвет фона окна
window.setup(width=600, height=600)  # задаем ширину и высоту окна
window.tracer(0)  # отключаем перерисовку
# window.bgpic("background.png") Можно положить в папку с кодом программы png картинку размером 600x600 и использовать ее как фон окна.

delay = 1 / 10  # частоты обновления экрана или паузу между перерисовками экрана

# голова змейки
head = turtle.Turtle('square')  # Создаем новый объект "Черепаха"
head.direction = 'stop'  # Добавляем ему поле direction где будем хранить текущее направление змейки
head.penup()  # этот метод отлючает отрисовку линии вслед за движение "Черепахи"
head.pencolor("green")  # Задаем цвет контура
head.fillcolor("black")  # Задаем цвет заливки
# head.color("green", "black") # Оба цвета можно задать также используя метод color

# Создание яблока
apple = turtle.Turtle("square")
apple.penup()
apple.pencolor("black")
apple.fillcolor("red")
# apple.color("black", "red")
apple.speed(0)
apple.goto(100, 100)


# Функция перемещает яблоко в новые координаты кратно размеру одного квадратика на поле
def move_apple_to_random_position():
    # размеры экрана 600х600
    # размеры квадратика (голова змейки, яблоко, часть хвоста) 20
    # значит нужно случайное число от 0 до 30
    # потому что 600 / 20 = 30
    step = 14
    rand_x = random.randint(-step, step) * 20 + 20
    rand_y = random.randint(-step, step) * 20 + 20
    apple.goto(rand_x, rand_y)
    print("rand_x: {}, rand_y: {}".format(rand_x, rand_y))


# Тут начинаются функции меняющие направление Змейки.
# Само по себе поле direction содержит лишь строку - название направления, например up или left
# Есть правило: Если Змейка едет влево, она не может развернуться и поехать вправо иначе она въедет в свой хвост, тоже для верх/низ направлений
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Это функция меняет одну из координат головы Змейки на расстояние равное размеру головы (или любой клетки игрового поля) - 20px
def move():
    if head.direction == "up":
        y = head.ycor()  # метод ycor возвращает y координату головы
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()  # метод xcor возвращает x координату головы
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Создаем коллекцию (список) в котором будем хранить сегменты (квадратики) хвоста
segments = []  # [turtle.Turtle]


# Эта функция создает новый объект "Черепаха" который будет являться сегментом хвоста Змейки
def create_new_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.fillcolor("grey")
    new_segment.pencolor(head.pencolor())
    new_segment.penup()
    return new_segment


# Эта функция добавляет новый сегмент в список сегментов
def add_segment():
    segments.append(create_new_segment())


def segment_shift(head_x, head_y):
    prev_x = head_x
    prev_y = head_y
    for segment in segments:
        curr_x = segment.xcor()
        curr_y = segment.ycor()
        segment.goto(prev_x, prev_y)
        prev_x = curr_x
        prev_y = curr_y


# Тут связываем нажатия клавишь клавиатуры с вызовом функций для управления Змейкой
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")
# window.onkeypress(add_segment, "space") # Тат можно потестировать добавление новых сегментов хвоста нажимая на пробел


# Функция проверяет столкнулась ли голова Змейки с яблоком и если да то добавляет Змейке новый сегмент хвоста и перемещает яблоко в новое место
def on_collision():
    if head.distance(apple) < 20:
        add_segment()
        move_apple_to_random_position()


# Остновно игровой цикл состоит из
while True:
    segment_shift(head.xcor(), head.ycor())  # изменения положения сегментов хвоста
    move()  # изменения положения головы
    on_collision()  # проверка столкновения с яблоком
    window.update()  # обновления экрана
    time.sleep(delay)  # вызова паузы между перерисовками экрана, чтоб контролировать скорость анимации
