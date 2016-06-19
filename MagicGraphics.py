# env/bin/python3
# Kuskova Natalia
import turtle
import json
import os

FUNCTIONS = {}
COMMANDS = ['new', 'save', 'open', 'edit', 'list']
FIGURES = []

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_turtle.hideturtle()
my_turtle.speed(0)


def functions(function):
    global FUNCTIONS
    FUNCTIONS[function.__name__] = function
    return functions


@functions
def triangle(*args):
    if args:
        points = args[0][0]
        color = args[0][1]
    else:
        points = list(map(int, input("Enter the coordinates of a triangle's "
                                     "vertices in the format: x1,y1,"
                                     "x2,y2,x3,y3\n").split(',')))
        quit_(points)
        color = input("Enter the fill color of the triangle: ")
        quit_(color)
    draw_triangle(points, color)
    return [points, color]


def draw_triangle(points, color):
    my_turtle.fillcolor(color)
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(points[0], points[1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[2], points[3])
    my_turtle.goto(points[4], points[5])
    my_turtle.goto(points[0], points[1])
    my_turtle.end_fill()


@functions
def rectangle(*args):
    if args:
        points = args[0][0]
        color = args[0][1]
    else:
        points = list(map(int, input("Enter the coordinates of a rectangle's "
                                     "vertices in the format: x1,y1,x2,y2,x3,"
                                     "y3,x4,y4\n").split(',')))
        quit_(points)
        color = input("Enter the fill color of the rectangle: ")
        quit_(color)
    draw_rectangle(points, color)
    return [points, color]


def draw_rectangle(points, color):
    my_turtle.fillcolor(color)
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(points[0], points[1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[2], points[3])
    my_turtle.goto(points[4], points[5])
    my_turtle.goto(points[6], points[7])
    my_turtle.goto(points[0], points[1])
    my_turtle.end_fill()


@functions
def circle(*args):
    if args:
        x = args[0][0]
        y = args[0][1]
        radius = args[0][2]
        angle = args[0][3]
        color = args[0][4]
    else:
        x = int(input("Enter the coordinate x: "))
        quit_(x)
        y = int(input("Enter the coordinate y: "))
        quit_(y)
        radius = int(input("Enter the radius of the circle: "))
        quit_(radius)
        angle = int(input("Enter the angle of the circle: "))
        quit_(angle)
        color = input("Enter the fill color of the circle: ")
        quit_(color)
    draw_circle(x, y, radius, angle, color)
    return [x, y, radius, angle, color]


def draw_circle(x, y, radius, angle, color):
    my_turtle.fillcolor(color)
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.circle(radius, angle)
    my_turtle.end_fill()


@functions
def dot(*args):
    if args:
        x = args[0][0]
        y = args[0][1]
        size = args[0][2]
        color = args[0][3]
    else:
        x = int(input("Enter the coordinate x: "))
        quit_(x)
        y = int(input("Enter the coordinate y: "))
        quit_(y)
        size = int(input("Enter the size: "))
        quit_(size)
        color = input("Enter the color of the point: ")
        quit_(color)
    draw_dot(x, y, size, color)
    return [x, y, size, color]


def draw_dot(x, y, size, color):
    my_turtle.fillcolor('#cdc9c9')
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.dot(size)
    my_turtle.end_fill()


@functions
def line(*args):
    if args:
        points = args[0][0]
        color = args[0][1]
    else:
        points = list(map(int, input("Enter the coordinates of a line's "
                                     "vertices in the format: x1,y1,"
                                     "x2,y2\n").split(',')))
        quit_(points)
        color = input("Enter the color of the line: ")
        quit_(color)
    draw_line(points, color)
    return [points, color]


def draw_line(points, color):
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(points[0], points[1])
    my_turtle.down()
    my_turtle.goto(points[2], points[3])


def edit_triangle():
    print("edit_triangle")


def new():
    my_turtle.clear()


def save(figures):
    file_name = input("Enter the file name: ")
    with open(file_name+'.json', 'w', encoding='utf-8') as f:
        json.dump(figures, f)
        f.close()
        print('File has been successfully saved.')


def open_():
    my_turtle.clear()
    file_name = input("Enter the file name: ")
    exists = os.path.exists(file_name+'.json')
    if exists:
        with open(file_name+'.json', 'r', encoding='utf-8') as f:
            entry = json.load(f)
            f.close()
            return entry


def edit():
    figure_name = input("Figure name: ")
    figure_name()


def list_of_figures():
    print("List of figures: ")
    for f in FIGURES:
        for figure_name in f:
            print("    " + figure_name)


def quit_(value):
    if value == 'quit':
        quit()


if __name__ == "__main__":
    print("Welcome to graphics editor MagicGraphics")
    print("Further is given a list of possible functions and commands:")
    print("\n")
    print("Functions:")
    for i in FUNCTIONS:
        print("    " + i)
    print("\n")
    print("Commands:")
    for j in COMMANDS:
        print("    " + j)
    print("\n")
    print("Enter 'quit' for exit.")
    print("\n")
    while True:
        function_name = input("Please, enter the name of the figure or "
                              "command: ")
        attributes = {}
        if function_name in FUNCTIONS:
            attributes[function_name] = FUNCTIONS[function_name]()
            FIGURES.append(attributes)
        elif function_name in COMMANDS:
            if function_name == 'new':
                new()
                attributes.clear()
                FIGURES.clear()
            elif function_name == 'save':
                save(FIGURES)
            elif function_name == 'open':
                picture = open_()
                if picture:
                    attributes.clear()
                    FIGURES.clear()
                    for i in picture:
                        for figure in i:
                            FUNCTIONS[figure](i[figure])
                        FIGURES.append(i)
                else:
                    print('No such file.')
            elif function_name == 'edit':
                edit()
            elif function_name == 'list':
                list_of_figures()
        elif function_name == 'quit':
            quit()
        else:
            print("Incorrect function.")

    # my_win.exitonclick()

    # turtle.done()
