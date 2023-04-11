mini = int(input('Enter MIN: '))
maxi = int(input('Enter MAX: '))
lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
filtered_list = [i for i in lst if mini <= i <= maxi]
sum_ = sum(filtered_list)
k = 1
product = 1
for i in filtered_list:
    if len(filtered_list) == 0:
        product = 0
    else:
        product = product * i * k  # k was added for cases where between mini and maxi only one element (another lst needed)
print(f'sum_ = {sum_}, product = {product}')
