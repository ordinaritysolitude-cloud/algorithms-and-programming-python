import datetime
import random

def check_dates(*dates):
    correct_dates = []

    for d in dates:
        try:
            date = datetime.date(*d)
            correct_dates.append(date)
        except ValueError:
            # Пропускаем некорректные даты
            continue

    if not correct_dates:
        return [], 0, None, None, []

    today = datetime.date.today()
    future_dates = [date for date in correct_dates if date > today]

    return correct_dates, len(correct_dates), min(correct_dates), max(correct_dates), sorted(future_dates)

def get_int_input(message, min=None, max=None):
    while True:
        try:
            user_input = input(message)
            try:
                val = int(user_input)
            except ValueError:
                raise ValueError("Пожалуйста, введите корректное целое число")

            if min is not None and val < min:
                raise ValueError(f"Число должно быть не меньше {min}")
            if max is not None and val > max:
                raise ValueError(f"Число должно быть не больше {max}")

            return val
        except ValueError as e:
            print("Ошибка:", e)

# Программа
print("--- Программа проверки сгенерированных дат ---")

dates_count = get_int_input("Введите количество дат для генерации: ", 1)

print("--- Настройка границ для ГОДА ---")
year_min = get_int_input("Минимум для года: ", 1)
year_max = get_int_input("Максимум для года: ", year_min)

print("--- Настройка границ для МЕСЯЦА ---")
month_min = get_int_input("Минимум для месяца: ", 1, 12)
month_max = get_int_input("Максимум для месяца: ", month_min, 12)

print("--- Настройка границ для ДНЯ ---")
day_min = get_int_input("Минимум для дня: ", 1, 31)
day_max = get_int_input("Максимум для дня: ", day_min, 31)

# Генерация дат
dates = []

for i in range(dates_count):
    d = (random.randint(year_min, year_max), random.randint(month_min, month_max), random.randint(day_min, day_max))
    dates.append(d)

# Проверка дат
correct_dates, count, min_date, max_date, future_dates = check_dates(*dates)

# Вывод результата
print("=== Результаты ===")

if count > 0:
    print("Все корректные даты:", [str(d) for d in correct_dates])
    print("Самая ранняя дата:", min_date)
    print("Самая поздняя дата:", max_date)
    print("Будущие даты относительно сегодня:", [str(d) for d in future_dates])
else:
    print("Корректных дат нет")

