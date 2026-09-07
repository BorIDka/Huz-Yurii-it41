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

# Створюємо масив rows форми (2, 12)
rows = np.array([
    temps,
    days_in_month
])

# Створюємо correction
correction = np.array([1, 0])

print("=" * 50)
print("ПЕРЕВІРКА BROADCASTING")
print("=" * 50)

print("\nФорма rows:", rows.shape)
print("Форма correction:", correction.shape)

# Спроба додавання
try:
    result = rows + correction
    print("\nРезультат:")
    print(result)

except ValueError as error:
    print("\nПомилка broadcasting:")
    print(error)


# Змінюємо форму correction
correction = correction.reshape(2, 1)

print("\nПісля reshape:")
print("Форма rows:", rows.shape)
print("Форма correction:", correction.shape)

# Повторне додавання
result = rows + correction

print("\nРезультат rows + correction:")
print(result)