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

month_numbers = np.arange(1, 13)


# Завдання 2
print("Температура в °C:")
print(temps)

# Переведення °C у °F
temps_f = temps * 9 / 5 + 32

print("\nТемпература в °F:")
print(temps_f)

# Кількість днів із температурою вище 15°C
warm_days = days_in_month[temps > 15].sum()

print("\nКількість днів із температурою вище 15°C:")
print(warm_days)

# Перевірка кількості днів у році
total_days = days_in_month.sum()

print("\nКількість днів у році:")
print(total_days)

print("Чи дорівнює 365:")
print(total_days == 365)