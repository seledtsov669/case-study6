"""Case-study Тесселяция
Разработчики:
Иванов А.С.,
Петров П.С.,
Сидоров C.H.
"""
import math
import turtle

def get_colours_choice():
    """Функция, получающая нужные цвета заливки"""

    # Вывести допустимые цвета
    l_c = ['зелёный', 'красный', 'золотистый', 'бирюзовый', 'жёлтый', 'серебряный']
    print('Допустимые цвета заливки:')
    for i in range(0, 6):
        print(l_c[i])

    # Предложить ввод цветов
    bl_c = ['зелёный','красный','золотистый','бирюзовый','жёлтый','серебряный', 'зеленый', 'желтый']
    first_colour = input('Пожалуйста, введите цвет: ')
    while not(first_colour.lower() in bl_c):
        print("'{}' не является верным значением. ".format(first_colour), end='')
        first_colour = input('Пожалуйста, введите цвет: ')
    else:
        second_colour = input('Пожалуйста, введите цвет: ')
        while not (second_colour.lower() in bl_c):
            print("'{}' не является верным значением. ".format(second_colour), end='')
            second_colour = input('Пожалуйста, введите цвет: ')
    if first_colour == 'зелёный' or 'зеленый':
        first_colour = 'green'
    if first_colour == 'жёлтый' or 'желтый':
        first_colour = 'yellow'
    if first_colour == 'бирюзовый':
        first_colour = 'paleturquoise'
    if first_colour == 'красный':
        first_colour = 'crimson'
    if first_colour == 'золотистый':
        first_colour = 'gold'
    if first_colour == 'серебряный':
        first_colour = 'silver'
    if second_colour == 'чёрный' or 'черный':
        second_colour = 'black'
    if second_colour == 'жёлтый' or 'желтый':
        second_colour = 'yellow'
    if second_colour == 'бирюзовый':
        second_colour = 'paleturquoise'
    if second_colour == 'красный':
        second_colour = 'crimson'
    if second_colour == 'золотистый':
        second_colour = 'gold'
    if second_colour == 'серебряный':
        second_colour = 'silver'
    return first_colour, second_colour

def get_num_hexagons():
    """Funktion getting number of hexagons in a raw"""
    num_hexagons = float(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
    while not (4 <= num_hexagons <= 20):
        num_hexagons = float(input('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: '))
    return num_hexagons

def draw_hexagon(x, y, side, color):
    '''
    Funktion drawing hexagon
    :param x: upper left corner coordinate X
    :param y: upper left corner coordinate Y
    :param side: side length of a hexagon
    :return: None
    '''
    turtle.home()
    turtle.up()
    turtle.setposition(x, y)
    turtle.left(90)
    turtle.color('black', color)

    turtle.down()
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(side)
        turtle.right(60)
    turtle.end_fill()
    turtle.up()

def draw_raw_hexagons(x, y, n):
    """Funktion drawing a raw of hexagons"""
    w = x
    e = y
    side_hexagon = math.floor(500 / (2 * n))
    for i in range(math.ceil(n / 2)):
        draw_hexagon(x, y, side_hexagon, 'red')
        #Получить координаты для следуующего шестиугольника
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()


    turtle.up()
    turtle.goto(w - side_hexagon * math.sqrt(3), e)

    for q in range(math.floor(n / 2)):
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()
        draw_hexagon(x, y, side_hexagon, 'black')

def draw_raw_hexagons1(x, y, n, color1, color2):
    """Funktion drawing a raw of hexagons"""
    w = x
    e = y
    side_hexagon = math.floor(500 / (2 * n))
    for i in range(math.ceil(n / 2)):
        draw_hexagon(x, y, side_hexagon, color2)
        #Получить координаты для следуующего шестиугольника
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()

    turtle.up()
    turtle.goto(w - side_hexagon * math.sqrt(3), e)

    for q in range(math.floor(n / 2)):
        x = turtle.xcor() + 2 * (side_hexagon * math.sqrt(3))
        y = turtle.ycor()
        draw_hexagon(x, y, side_hexagon, color1)

def main(x, y):
    """Funktion making tessellation"""
    q = x
    m = y
    n = get_num_hexagons()
    side_hexagon = math.ceil(500 / (2 * n))
    d = side_hexagon * math.sqrt(3)
    h = side_hexagon / 2
    draw_raw_hexagons(x, y, n)
    if n % 2 == 0:
        p = n / 2
        for t in range(int(p)):
            draw_raw_hexagons(x, y, n)
            x = turtle.xcor()
            y = turtle.ycor() + (h + side_hexagon) * 2
            draw_raw_hexagons1(x, y, n)
            x = turtle.xcor()
            y = turtle.ycor() + (h + side_hexagon) * 2
            turtle.up()
            turtle.goto(x, y)
            turtle.down()

        turtle.up()
        turtle.goto(q + d / 2, m + side_hexagon + h)
        x = turtle.xcor()
        y = turtle.ycor()

        for r in range(int(p)):
            draw_raw_hexagons(x, y, n)
            x = turtle.xcor()
            y = turtle.ycor() + (h + side_hexagon) * 2
            draw_raw_hexagons1(x, y, n)
            x = turtle.xcor()
            y = turtle.ycor() + (h + side_hexagon) * 2



turtle.speed(970)
#main(-250, -250)
#draw_raw_hexagons(0, 0, 13)
j = get_colours_choice()
color1 = j[0]
color2 = j[1]
print(color1)
print(color2)
#draw_raw_hexagons1(0, 0, 13, color1, color2)
turtle.mainloop()