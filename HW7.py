size = int(input("Enter size of triangle: "))
for i in range(1, size + 1):
    print(" " * (size - i) + "*" * i)
