import random


def get_random_string(length: int):
    i = 0
    result = ''
    while i < length:
        random_lst = ([random.randrange(48, 57), random.randrange(65, 90), random.randrange(97, 122)])
        random_val = random.choice(random_lst)
        random_char = chr(random_val)
        result += random_char
        i += 1
    return result


