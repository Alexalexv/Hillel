a = int(input('input a: '))
b = int(input('input b: '))
c = int(input('input c: '))

if a > b and a > c:
    print(f'Max value is a = {a}')
elif b > a and b > c:
    print(f'Max value is b = {b}')
elif c > a and c > b:
    print(f'Max value is c = {c}')
elif a == b == c:
    print(f'All values are equal')
elif a == b and a > c:
    print(f'Max are a and b = {a}')
elif a == c and a > b:
    print(f'Max are a and c = {a}')
elif b == c and b > a:
    print(f'Max are b and c = {b}')
