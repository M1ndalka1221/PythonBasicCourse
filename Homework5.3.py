import string

users_string = input("Enter a string: ")

titled_string = users_string.title()

clean_string = "".join([symbol for symbol in titled_string if not symbol.isspace() and symbol not in string.punctuation])

hashtag = "#" + clean_string

hashtag = hashtag[:140]
print(hashtag)
