def common_elements():
    list_multiples_three = [x for x in range(100) if x % 3 == 0]
    list_multiples_five = [x for x in range(100) if x % 5 == 0]

    set_multiples_three = set(list_multiples_three)
    set_multiples_five = set(list_multiples_five)

    return set_multiples_three.intersection(set_multiples_five)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")