string = input("Please enter your string: ").strip().lower()
print(f'It`s palindrome') if string == string[::-1] else print(f'It isn`t palindrome')
