import numpy as np

# Варіант 3 — Одеса

# Температури за місяцями
temps = np.array([
    -1, 0, 4, 10, 16, 20,
    23, 22, 17, 11, 5, 1
])

# Кількість днів у місяцях
days_in_month = np.array([
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
])

# Третій рядок — умовна кількість сонячних годин
sun_hours = np.array([
    80, 95, 140, 190, 240, 270,
    300, 280, 220, 170, 110, 75
])

# Створення двовимірного масиву
data = np.array([
    temps,
    days_in_month,
    sun_hours
])

print("=" * 50)
print("ЗАВДАННЯ 4 — ДВОВИМІРНИЙ МАСИВ")
print("=" * 50)

print("\nДвовимірний масив data:")
print(data)

print("\nФорма масиву:")
print(data.shape)

# Сума по кожному рядку
print("\nСума по кожному рядку (axis=1):")
print(data.sum(axis=1))

# Середнє по кожному рядку
print("\nСереднє по кожному рядку (axis=1):")
print(data.mean(axis=1))

# Сума по кожному стовпцю
print("\nСума по кожному стовпцю (axis=0):")
print(data.sum(axis=0))

# Сума для січня
january_sum = data[:, 0].sum()

print("\nСума для першого стовпця (січень):")
print(january_sum)

print("\nРозрахунок:")
print(
    temps[0],
    "+",
    days_in_month[0],
    "+",
    sun_hours[0],
    "=",
    january_sum
)