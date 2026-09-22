TASKS_COUNT = 20 # Кол-во задач всего
STUDENTS_COUNT = 19 # Кол-во студентов
VARIANT_COUNT = 5 # Кол-во задач в варианте для студента

import random

random.seed(42)

tasks = [i for i in range(1,TASKS_COUNT+1)]
variants = []

for i in range(1, STUDENTS_COUNT+1):
    t = random.sample(tasks, k=VARIANT_COUNT)
    variants.append(t)
    print(f"Студент {i}: {t}")

#print(variants)