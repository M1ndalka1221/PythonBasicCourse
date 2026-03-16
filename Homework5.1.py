import keyword
import string

user_variable = input("Enter a name for variable: ")
is_valid = True

if user_variable[0].isdigit():
    is_valid = False

for letter in user_variable:
    if letter.isupper():
        is_valid = False
        break

    if letter in string.punctuation.replace("_", ""):
        is_valid = False
        break

    if letter.isspace():
        is_valid = False

if user_variable.count("_") == len(user_variable) and len(user_variable) > 1:
    is_valid = False

elif user_variable in keyword.kwlist:
    is_valid = False

print(is_valid)




