mini = int(input('Enter minimal width: '))
maxi = int(input('Enter maximal width: '))
half = (maxi - mini) // 2

if mini > maxi:
    print(f'Maximal width ({maxi}) less than minimal width ({mini})')

elif (maxi - mini) % 2 != 0:
    print(f'Difference between {maxi} and {mini} is not multiple to two')

elif maxi == mini and maxi > 2: #це для квадратів :))
    print(' ' * (half) + mini * '*')
    for i in range(maxi - 2):
        print('*' + ' ' * (maxi - 2) + '*')
    print(' ' * (half) + mini * '*')

else:
    print(' ' * (half) + mini * '*')
    for i in range(half):
        print(' ' * (half - (i + 1)) + '*' + ' ' * (maxi - max(2 * (half - (i + 1)), 0) - 2) + '*')
    for i in range(half - 2, -1, -1):
        print(' ' * ((maxi - mini) // 2 - (i + 1)) + '*' + ' ' * (maxi - max(2 * (half - (i + 1)), 0) - 2) + '*')
    print(' ' * half + mini * '*')
