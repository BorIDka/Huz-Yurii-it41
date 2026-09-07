# Варіант 3 — Одеса

import numpy as np

temps = np.array([-3, -2, 2, 8, 13, 16, 18, 17, 13, 8, 3, -1])

days_in_month = np.array([
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
])

month_numbers = np.arange(1, 13)

print("Температури:")
print(temps)
print("shape:", temps.shape)
print("dtype:", temps.dtype)

print("\nКількість днів у місяцях:")
print(days_in_month)
print("shape:", days_in_month.shape)
print("dtype:", days_in_month.dtype)

print("\nНомери місяців:")
print(month_numbers)
print("shape:", month_numbers.shape)
print("dtype:", month_numbers.dtype)