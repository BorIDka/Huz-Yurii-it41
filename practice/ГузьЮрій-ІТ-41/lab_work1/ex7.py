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

print("=" * 50)
print("ЗАВДАННЯ 5 — RESHAPE І BROADCASTING")
print("=" * 50)

# Створюємо масив форми (2, 12)
rows = np.array([
    temps,
    days_in_month
])

print("\nМасив rows:")
print(rows)

print("\nФорма rows:")
print(rows.shape)

# Створюємо correction
correction = np.array([1, 0])

print("\nМасив correction:")
print(correction)

print("Форма correction:")
print(correction.shape)


# Спроба додати correction
print("\nСпроба виконати rows + correction:")

try:
    result = rows + correction
    print(result)
except ValueError as error:
    print("Виникла помилка broadcasting!")
    print(error)


# Змінюємо форму correction
correction_reshaped = correction.reshape(2, 1)

print("\nПісля reshape(2, 1):")
print(correction_reshaped)

print("Нова форма:")
print(correction_reshaped.shape)


# Додаємо масиви
result = rows + correction_reshaped

print("\nРезультат rows + correction.reshape(2, 1):")
print(result)