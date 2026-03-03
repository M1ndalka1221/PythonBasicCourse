# 1. Квадрат числа.
# Користувач вводить число. Програма виводить його квадрат.
# Приклад:
# Введіть число: 5
# Квадрат числа: 25

number = int(input("Enter a number: "))
print(f"Answer is: {number**2}")

# 2. “Середнє трьох чисел”
# Програма запитує три числа і виводить їх середнє арифметичне.
# Приклад:
# Введіть три числа: 2, 4, 6
# Середнє: 4.0

first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))
third_number = int(input("Enter a third number: "))
result = (first_number + second_number + third_number) / 3
print(f"Answer is: {result}")

# 3. “Перетворення хвилин у години”
# Користувач вводить кількість хвилин. Програма виводить, скільки це годин і хвилин.
# Приклад:
# Введіть кількість хвилин: 135
# 2 години 15 хвилин

amount_of_minutes = int(input("Enter how many minutes: "))
amount_of_hours = amount_of_minutes // 60
amount_of_minutes_left = amount_of_minutes % 60
print(f"{amount_of_hours} hours and {amount_of_minutes_left} minutes")