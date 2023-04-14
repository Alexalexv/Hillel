len_ = 0
str_ = ''
with open('file', 'r') as f:
    for line in f:
        line_len = len(line)
        if line_len > len_:
            len_ = line_len
            str_ = line

print(str_)
