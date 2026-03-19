users_number = int(input("Enter amount of seconds between 0 and 8640000: "))

if 0 <= users_number < 8640000:
    days, remainder_of_number = divmod(users_number, 86400)
    hours, remainder_of_number = divmod(remainder_of_number, 3600)
    minutes, secs = divmod(remainder_of_number, 60)

    last_digit = days % 10
    last_two_digits = days % 100

    if 11 <= last_two_digits <= 14:
        day_word = "днів"
    elif last_digit == 1:
        day_word = "день"
    elif 2 <= last_digit <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"
    print(f"{days} {day_word}, {time_str}")

else:
    print("Enter a correct number")



