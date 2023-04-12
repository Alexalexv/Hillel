lst = [['a', 'c', 'd'],
       ['f', 'b', 'a'],
       ['a', 'n', 'k'],
       ['e', 'l', 'i']]

row_count = len(lst)
column_count = len(lst[0])

transposed_lst = []
for c in range(column_count):
    transposed_row = []
    for r in range(row_count):
        transposed_row.append(lst[r][c])
    transposed_lst.append(transposed_row)

sorted_transposed_lst = []
for i in transposed_lst:
    i.sort()
    sorted_transposed_lst.append(i)

row_count_transposed = len(transposed_lst)
column_count_transposed = len(transposed_lst[0])

sorted_list = []
for c in range(column_count_transposed):
    sorted_row = []
    for r in range(row_count_transposed):
        sorted_row.append(sorted_transposed_lst[r][c])
    sorted_list.append(sorted_row)
print(sorted_list)
