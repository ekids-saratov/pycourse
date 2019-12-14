import time
import turtle

# Конфигурируем экран программы, задаем начальные свойства
window = turtle.Screen()  # Создаем экземпляр класса (объект) Screen и прискаеваем его в переменную window
window.title('Snake Game')  # Задаем заголовок окна
window.bgcolor('green')  # Задаем цвет фона окна
window.setup(width=600, height=600)  # задаем ширину и высоту окна
window.tracer(0)  # отключаем перерисовку, потому что будем перерисовывать вызывая window.uodate() явным образом

# голова змейки
head = turtle.Turtle('square')  # Создаем новый объект "Черепаха"
head.direction = 'stop'  # Добавляем ему поле direction где будем хранить текущее направление змейки
head.penup()  # этот метод отлючает отрисовку линии вслед за движение "Черепахи"


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
        head.sety(head.ycor() - 20)  # Так можно немного оптимизировать код убрав одну строку

    if head.direction == "left":
        x = head.xcor()  # метод xcor возвращает x координату головы
        head.setx(x - 20)

    if head.direction == "right":
        head.setx(head.xcor() + 20)


# Тут связываем нажатия клавишь клавиатуры с вызовом функций для управления Змейкой
window.listen()  # эта функция влкючает прослушивание нажатий клавиатуры и мыши
window.onkeypress(go_up, "Up")  # когда клавиша Вверх нажата вызови функцию go_up
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Остновно игровой цикл состоит из
while True:
    window.update()  # обновления экрана,
    move()  # изменения положения головы
    time.sleep(1 / 10)  # вызова паузы между перерисовками экрана, чтоб контролировать скорость анимации
