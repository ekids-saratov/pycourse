import time
import turtle

# Конфигурируем экран программы, задаем начальные свойства
window = turtle.Screen()  # Создаем экземпляр класса (объект) Screen и прискаеваем его в переменную window
window.title('Snake Game')  # Задаем заголовок окна
window.bgcolor('#8b1c71')  # Задаем цвет фона окна
window.setup(width=600, height=600)  # задаем ширину и высоту окна
window.tracer(0)  # отключаем перерисовку, потому что будем перерисовывать вызывая window.uodate() явным образом
# window.bgpic("background.png") #  Можно положить в папку с кодом программы png картинку размером 600x600 и использовать ее как фон окна.

delay = 1 / 10  # частоты обновления экрана или паузу между перерисовками экрана

# голова змейки
head = turtle.Turtle('square')  # Создаем новый объект "Черепаха"
head.direction = 'stop'  # Добавляем ему поле direction где будем хранить текущее направление змейки
head.penup()  # этот метод отлючает отрисовку линии вслед за движение "Черепахи"
head.pencolor("green")  # Задаем цвет контура
head.fillcolor("black")  # Задаем цвет заливки
# head.color("green", "black") # Оба цвета можно задать также используя метод color


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
segments = []  # [turtle.Turtle]  # Можно явно указать какого типа объекты будут в списке чтоб получить подсказки о доступных в них своиствах


# Эта функция создает новый объект "Черепаха" который будет являться сегментом хвоста Змейки
def create_new_segment():
    new_segment = turtle.Turtle()  # Создаем новый объект "Черепаха". НЕ ЗАБЫВАЙТЕ СТАВИТЬ КРУГЛЫЕ СКОБКИ ПОСЛЕ .Turtle
    # Задаем скорость анимации
    new_segment.speed(0)  # в данном случае отключаем анимацию рисования линии и поворота "Черепахи" Это ускоряет выполнение кода
    new_segment.shape("square")
    new_segment.fillcolor("grey") # Цвета можно задавать динамически, тогда каждый новый сегмент будет отличаться
    new_segment.pencolor(head.pencolor())
    new_segment.penup()  # Не будем рисовать линию при перемещении "Черепахи"
    return new_segment


# Эта функция добавляет новый сегмент в список сегментов
def add_segment():
    segments.append(create_new_segment())


# Эта функция сдвигает сегменты хвоста на новое положение
# Запоминаются текущие координаты сегмента ему присваиваются координаты предидущего сегмента , а первому сегменту присваиваются координаты головы Змейки
def segment_shift(head_x, head_y):
    prev_x = head_x  # prev - previous предидущий
    prev_y = head_y
    for segment in segments:
        curr_x = segment.xcor()  # curr - current текущий
        curr_y = segment.ycor()
        segment.goto(prev_x, prev_y)
        prev_x = curr_x
        prev_y = curr_y


# Тут связываем нажатия клавишь клавиатуры с вызовом функций для управления Змейкой
window.listen()  # эта функция влкючает прослушивание нажатий клавиатуры и мыши
window.onkeypress(go_up, "Up")  # когда клавиша Вверх нажата вызови функцию go_up
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

window.onkeypress(add_segment, "space")  # Так можно протестировать добавление новых сегментов хвоста нажимая на пробел

# Остновно игровой цикл состоит из
while True:
    window.update()  # обновления экрана,
    segment_shift(head.xcor(), head.ycor())  # изменения положения сегментов хвоста
    move()  # изменения положения головы
    time.sleep(delay)  # вызова паузы между перерисовками экрана, чтоб контролировать скорость анимации
