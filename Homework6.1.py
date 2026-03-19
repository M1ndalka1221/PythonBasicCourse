import string

print("Enter 'quit' to exit.")

while True:
    users_string = input("Enter dwo letters separated by - : ")

    if users_string == "quit":
        print("Goodbye!")
        break

    if len(users_string) != 3 or users_string[1] != "-":
        print("Invalid input. Please enter only dwo letters separated by - ")
        continue

    else:
        first_letter, second_letter = users_string.split("-")

        if first_letter not in string.ascii_letters or second_letter not in string.ascii_letters:
            print("Enter a correct letters")
            continue

        else:
            first_letter_index = string.ascii_letters.index(first_letter)
            second_letter_index = string.ascii_letters.index(second_letter)
            if first_letter_index <= second_letter_index:
                result = string.ascii_letters[first_letter_index:second_letter_index + 1]
            else:
                result = string.ascii_letters[second_letter_index:first_letter_index + 1][::-1]

            print(result)

