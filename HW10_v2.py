user_input = input("Please enter your string: ")
string = user_input.strip().lower()
splitted_string = list(string)
reversed_splitted_string = []

for i in splitted_string:
    reversed_splitted_string.insert(0, i)
else:
    reversed_string = ''.join(reversed_splitted_string)

if reversed_string == string:
    print(f'"{user_input}" is palindrome')
else:
    print(f'"{user_input}" isn`t palindrome')
