# env/bin/python
# Kuskova Natalia
import turtle

FUNCTIONS = ['triangle', 'rectangle', 'circle', 'dot', 'line']

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_turtle.hideturtle()
my_turtle.speed(0)


def triangle(points, color):
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


def rectangle(points, color):
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


def circle(x, y, radius, angle, color):
    my_turtle.fillcolor(color)
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.circle(radius, angle)
    my_turtle.end_fill()


def dot(x, y, size, color):
    my_turtle.fillcolor(color)
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.dot(size)
    my_turtle.end_fill()


def line(points, color):
    my_turtle.pencolor(color)
    my_turtle.up()
    my_turtle.goto(points[0], points[1])
    my_turtle.down()
    my_turtle.goto(points[2], points[3])


def quit_(value):
    if value == 'quit':
        quit()


if __name__ == "__main__":

    print("Welcome to graphics editor MagicGraphics")
    print("Further is given a list of possible functions:")
    print("\n")
    for i in FUNCTIONS:
        print("    " + i)
    print("\n")
    print("Enter 'quit' for exit.")
    print("\n")
    while True:
        figure_name = input("Please, enter the name of the figure: ")

        if figure_name in FUNCTIONS:
            if figure_name == 'triangle':
                point = list(map(int, input("Enter the coordinates of a triangle's vertices "
                                            "in the format: x1,y1"
                                            "x2,y2,x3,y3\n").split(',')))
                quit_(point)
                fill_color = input("Enter the fill color of the triangle: ")
                quit_(fill_color)
                triangle(point, fill_color)
            elif figure_name == 'rectangle':
                point = list(map(int, input("Enter the coordinates of a rectangle's vertices "
                                            "in the format: x1,y1,x2,y2,x3,y3,x4,y4\n").split(',')))
                quit_(point)
                fill_color = input("Enter the fill color of the rectangle: ")
                quit_(fill_color)
                rectangle(point, fill_color)
            elif figure_name == 'circle':
                x_ = int(input("Enter the coordinate x: "))
                quit_(x_)
                y_ = int(input("Enter the coordinate y: "))
                quit_(y_)
                radius_ = int(input("Enter the radius of the circle: "))
                quit_(radius_)
                angle_ = int(input("Enter the angle of the circle: "))
                quit_(angle_)
                fill_color = input("Enter the fill color of the circle: ")
                quit_(fill_color)
                circle(x_, y_, radius_, angle_, fill_color)
            elif figure_name == 'dot':
                x_ = int(input("Enter the coordinate x: "))
                quit_(x_)
                y_ = int(input("Enter the coordinate y: "))
                quit_(y_)
                size_ = int(input("Enter the size: "))
                quit_(size_)
                fill_color = input("Enter the color of the point: ")
                quit_(fill_color)
                dot(x_, y_, size_, fill_color)
            elif figure_name == 'line':
                point = list(map(int, input("Enter the coordinates of a line's vertices "
                                            "in the format: x1,y1,"
                                            "x2,y2\n").split(',')))
                quit_(point)
                fill_color = input("Enter the color of the line: ")
                quit_(fill_color)
                line(point, fill_color)
        elif figure_name == 'quit':
            quit()
        else:
            print("Incorrect function.")

    my_win.exitonclick()

    # turtle.done()
