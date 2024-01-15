import turtle


def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order - 1, size / 3)
            turtle.left(angle)


def main():
    recursion_level = int(input("Рівень рекурсії"))
    window = turtle.Screen()
    window.bgcolor("white")
    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(2)
    initial_size = 300
    fractal_turtle.penup()
    fractal_turtle.goto(-initial_size / 2, -initial_size / 6)
    fractal_turtle.pendown()
    for _ in range(3):
        koch_snowflake(fractal_turtle, recursion_level, initial_size)
        fractal_turtle.right(120)
    window.exitonclick()


if __name__ == "__main__":
    main()
