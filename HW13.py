user_input = input('Please, input email for validation: ')

if user_input.count('@') != 1 or user_input.count('.') != 1:
    print(f'Please, check symbols "@" or "." in yours email "{user_input}"')
elif user_input.index('@') > user_input.index('.'):
    print(f'Symbols "@" and "." has wrong order in yours email "{user_input}"')
elif user_input[0] != '@' or user_input[-1] != '.':
    print(f'Your email "{user_input}" starts or ends with characters "@" or "."')
else:
    print(f'Our script is not perfect, but perhaps your email "{user_input}" is valid')

# testdata
# sasha@mail.ua sasha@@mail.ua sasha@mail..ua sasha.mail@ua @sasha.ua sasha@mail.
