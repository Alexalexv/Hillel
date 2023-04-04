n = int(input("Enter n: "))

for i in range(1, n + 1):
    left = list(range(1, i + 1))
    right = list(range(i - 1, 0, -1))
    left_str = ' '.join(map(str, left))
    right_str = ' '.join(map(str, right))
    print('  '*(n-i)+left_str, right_str)
