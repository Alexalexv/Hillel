def custom_map(func, *seq):
    result = list(map(func, *seq))
    return result


print(custom_map(sum, [[1, 2, 3], [4, 5]]))
print(custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)))
