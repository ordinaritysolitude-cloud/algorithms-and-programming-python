import math

# Solve quadratic equation, print roots
def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Equation is not quadratic (a=0)")

    d = b**2 - 4*a*c
    if d < 0:
        print("No solution")
    elif d == 0:
        x = -b / (2 * a)
        print("x =", x)
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)

def get_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a number")


print("--- Программа для решения квадратных уравнений ax² + bx + c = 0 ---")

try:
    # Вводим коэффициенты с проверкой типа данных
    a = get_input("Введите коэффициент a: ")
    b = get_input("Введите коэффициент b: ")
    c = get_input("Введите коэффициент c: ")

    solve_quadratic(a, b, c)
except ValueError as e:
    print(e)

