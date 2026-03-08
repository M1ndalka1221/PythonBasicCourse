users_list = [12, 3, 4, 10, 8]
if len(users_list) <= 1:
    print(users_list)
else:
    new_list = [users_list[-1]] + users_list[:-1]
    print(new_list)
