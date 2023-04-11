input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

first = [i for i in input_list if i % 3 == 0 and i % 5 != 0]
second = [i for i in input_list if i % 5 == 0 and i % 3 != 0]
third = [i for i in input_list if i % 5 == 0 and i % 3 == 0]

print(first)
print(second)
print(third)
