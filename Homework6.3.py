users_number = int(input("Enter a number: "))
current_number_str = str(users_number)

while int(current_number_str) > 9:
    product = 1

    for digit in current_number_str:
        product *= int(digit)

    current_number_str = str(product)

print(current_number_str)