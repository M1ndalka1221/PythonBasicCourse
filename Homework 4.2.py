numbers = [0, 1, 7, 2, 4, 8]

if len(numbers) == 0:
    print(0)
else:
    sum_of_even_numbers = sum(numbers[::2])
    result = sum_of_even_numbers * numbers[-1]
    print(result)