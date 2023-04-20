def read_last(file_path, symbol_number):
    with open(file_path, 'r') as f:
        for line in f:
            if len(line.strip()):
                line_ = line.replace('\n', '')
                print(line_[-symbol_number:])


read_last('read_last.txt', 6)
