import turtle

def factorial(n):
    """Returns the factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def draw_tree(branch_length, t):
    """Draws a fractal tree recursively."""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_tree(branch_length - 15, t)
        t.left(40)
        draw_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

def dragon_curve(t, length, depth, sign=1):
    """Draws a dragon curve recursively."""
    if depth == 0:
        t.forward(length)
    else:
        t.right(45 * sign)
        dragon_curve(t, length / 1.4142, depth - 1, 1)
        t.left(90 * sign)
        dragon_curve(t, length / 1.4142, depth - 1, -1)
        t.right(45 * sign)

def fractal_flower(t, petals, size, depth):
    """Draws a fractal flower with circular petals."""
    if depth == 0:
        return
    for _ in range(petals):
        t.circle(size)
        t.left(360 / petals)
        fractal_flower(t, petals, size * 0.5, depth - 1)

def draw_triangle(points, t, color):
    """Draws a filled triangle."""
    t.fillcolor(color)
    t.up()
    t.goto(points[0])
    t.down()
    t.begin_fill()
    t.goto(points[1])
    t.goto(points[2])
    t.goto(points[0])
    t.end_fill()

def midpoint(p1, p2):
    """Returns the midpoint between two points."""
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, depth, t):
    """Draws a Sierpinski triangle recursively."""
    colors = ["blue", "red", "green", "yellow", "orange", "purple", "pink"]
    draw_triangle(points, t, colors[depth % len(colors)])
    if depth > 0:
        sierpinski([points[0], midpoint(points[0], points[1]), midpoint(points[0], points[2])], depth - 1, t)
        sierpinski([points[1], midpoint(points[0], points[1]), midpoint(points[1], points[2])], depth - 1, t)
        sierpinski([points[2], midpoint(points[2], points[1]), midpoint(points[0], points[2])], depth - 1, t)


def main_menu():
    while True:
        print("\n🌟 Welcome to the Recursive Artistry Program! 🌟")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci Number")
        print("3. Draw a Fractal Tree")
        print("4. Draw a Dragon Curve")
        print("5. Draw a Fractal Flower")
        print("6. Draw a Sierpinski Triangle")
        print("7. Exit")

        choice = input("> ")

        if choice == '1':
            num = input("Enter a non-negative integer to find its factorial: ")
            if not num.isdigit() or int(num) < 0:
                print("❌ Invalid input. Please enter a non-negative integer.")
                continue
            num = int(num)
            print(f"The factorial of {num} is {factorial(num)}.")

        elif choice == '2':
            num = input("Enter a non-negative integer for Fibonacci: ")
            if not num.isdigit() or int(num) < 0:
                print("❌ Invalid input. Please enter a non-negative integer.")
                continue
            num = int(num)
            print(f"The {num}th Fibonacci number is {fibonacci(num)}.")

        elif choice == '3':
            print("Drawing a Fractal Tree... Close the window to return.")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.color("green")
            t.left(90)
            t.speed(0)
            draw_tree(100, t)
            turtle.done()

        elif choice == '4':
            print("Drawing a Dragon Curve... Close the window to return.")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.speed(0)
            t.penup()
            t.goto(-200, 0)
            t.pendown()
            dragon_curve(t, 400, 10)
            turtle.done()

        elif choice == '5':
            print("Drawing a Fractal Flower... Close the window to return.")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.speed(0)
            fractal_flower(t, petals=6, size=80, depth=3)
            turtle.done()

        elif choice == '6':
            print("Drawing a Sierpinski Triangle... Close the window to return.")
            screen = turtle.Screen()
            t = turtle.Turtle()
            t.speed(0)
            points = [(-200, -100), (0, 200), (200, -100)]
            sierpinski(points, 4, t)
            turtle.done()

        elif choice == '7':
            print("Thank you for using the Recursive Artistry Program. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main_menu()
