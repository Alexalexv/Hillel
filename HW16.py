lst = [3.5, 2, 4, 6.2, 8]
len_ = len(lst)
lst2 = [lst[0]]
for i in range(len_ - 1):
    avg = (lst[i] + lst[i + 1]) / 2
    lst2.append(avg)
    lst2.append(lst[i + 1])
print(lst2)
