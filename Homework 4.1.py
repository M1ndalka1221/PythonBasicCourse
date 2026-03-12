numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zeros = []
for number in numbers:
    if number != 0:
        non_zeros.append(number)
result = non_zeros + [0] * numbers.count(0)
print(result)