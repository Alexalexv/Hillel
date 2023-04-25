def gen(m, n):
    for i in range(1, n + 1):
        yield i
    exp = 2
    for i in range(1, n + 1):
        if exp <= m:
            yield i ** exp
            exp += 1
        else:
            yield i ** m
