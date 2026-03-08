first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
users_choice = int(input("Make a choice of the mathematical operation:\n"
                         "1 - Addition\n"
                         "2 - Subtraction\n"
                         "3 - Multiplication\n"
                         "4 - Division\n"))
match users_choice:
    case 1:
        print(first_number + second_number)
    case 2:
        print(first_number - second_number)
    case 3:
        print(first_number * second_number)
    case 4:
        if second_number == 0:
            print("Enter a correct number")
        else:
            print(first_number / second_number)
