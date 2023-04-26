def generator(m, n):
    for i in range(1, m + 1):
        for a in range(1, n + 1):
            yield a ** i


for i in generator(2, 2):
    print(i)
