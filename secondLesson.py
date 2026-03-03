number = int(input("Enter a number: "))
first_digit = number // 100
second_digit = number % 100 // 10
third_digit = number % 10
print(f"{first_digit}, {second_digit}, {third_digit}")