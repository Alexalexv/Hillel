len_ = 0
with open('file', 'r', ) as f:
    for line in f:
        line_len = len(line)
        if line_len > len_:
            len_ = line_len

print(f'Max length of string in file is {len_}')
