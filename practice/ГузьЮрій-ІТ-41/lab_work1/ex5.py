import numpy as np

# Варіант 3 — Одеса

temps = np.array([
    -1, 0, 4, 10, 16, 20,
    23, 22, 17, 11, 5, 1
])

month_numbers = np.arange(1, 13)


# Завдання 3
print("=" * 50)
print("ЗАВДАННЯ 3 — ІНДЕКСАЦІЯ І ФІЛЬТРАЦІЯ")
print("=" * 50)


# Найтепліший місяць
warmest_index = temps.argmax()
warmest_temp = temps[warmest_index]
warmest_month = month_numbers[warmest_index]

print("\nНайтепліший місяць:")
print("Номер місяця:", warmest_month)
print("Температура:", warmest_temp, "°C")
print("Індекс:", warmest_index)


# Найхолодніший місяць
coldest_index = temps.argmin()
coldest_temp = temps[coldest_index]
coldest_month = month_numbers[coldest_index]

print("\nНайхолодніший місяць:")
print("Номер місяця:", coldest_month)
print("Температура:", coldest_temp, "°C")
print("Індекс:", coldest_index)


# Місяці, де температура нижче 0°C
negative_months = month_numbers[temps < 0]

print("\nМісяці з температурою нижче 0°C:")
print(negative_months)


# Температури, відсортовані за зростанням
sorted_temps = np.sort(temps)

print("\nТемператури за зростанням:")
print(sorted_temps)


# Перевірка, що temps не змінився
print("\nОригінальний масив temps:")
print(temps)