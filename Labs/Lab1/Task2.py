import statistics
import random

def calculate(*args, mode="basic"):
    if not args:
        raise ValueError("Список чисел пуст")

    if not mode in ["basic", "advanced", "scientific"]:
        raise ValueError("Неизвестный режим работы")

    calculations = {}

    # Calculate basic (always)
    calculations["Максимум"] = max(args)
    calculations["Минимум"] = min(args)
    calculations["Среднее арифметическое"] = statistics.mean(args)

    if mode == "advanced" or mode == "scientific":
        calculations["Медиана"] = statistics.median(args)
        calculations["Мода"] = statistics.mode(args)

    if mode == "scientific":
        calculations["Среднее геометрическое"] = statistics.geometric_mean(args)
        calculations["Среднее гармоническое"] = statistics.harmonic_mean(args)

    return calculations

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Некорректное число")

try:
    count = int(get_number("Введите количество чисел для генерации: "))
    if count <= 0:
        raise ValueError("Количество чисел должно быть больше нуля")

    low = get_number("Нижняя граница генерации: ")
    high = get_number("Верхняя граница генерации: ")
    if low >= high:
        raise ValueError("Нижняя граница должна быть меньше верхней")

    mode = input("Введите режим (basic, advanced, scientific): ")

    # Генерируем случайные числа
    numbers = [random.uniform(low, high) for i in range(count)]
    calculations = calculate(*numbers, mode=mode)

    print("Сгенерированные числа: ", [round(n, 2) for n in numbers])

    print("[")
    for i, k in calculations.items():
        print(f"{i}: {k}")
    print("]")

except ValueError as e:
    print(e)