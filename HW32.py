def custom_map(func, *seq):
    if len(seq) == 1:
        result = []
        for i in list(*seq):
            result.append(func(i))
        return result
    else:
        result = []
        for i in zip(*seq):
            result.append(func(*i))
        return result


print(custom_map(sum, [[1, 2, 3], [4, 5]]))
print(custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)))
