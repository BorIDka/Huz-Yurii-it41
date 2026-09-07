import numpy as np

# Варіант 3 — Одеса

temps = np.array([
    -1, 0, 4, 10, 16, 20,
    23, 22, 17, 11, 5, 1
])

days_in_month = np.array([
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
])

# Створюємо масив rows
rows = np.array([
    temps,
    days_in_month
])

# Створюємо correction
correction = np.array([1, 0])

print("=" * 50)
print("ЗАВДАННЯ 5 — RESHAPE І BROADCASTING")
print("=" * 50)

print("\nФорма rows:")
print(rows.shape)

print("\nФорма correction:")
print(correction.shape)

# Перетворюємо correction з (2,) у (2, 1)
correction_2d = correction.reshape(2, 1)

print("\ncorrection після reshape(2, 1):")
print(correction_2d)

print("\nНова форма correction:")
print(correction_2d.shape)

# Виконуємо додавання
result = rows + correction_2d

print("\nРезультат:")
print(result)