s = "aab qq c badcc a qqqqqaqqqqaa tpara"
s_lst = s.split(' ')
result_lst = []
for i in s_lst:
    if i.count('a') == 2:
        result_lst.append(i)
    else:
        continue

result = ' '.join(result_lst).title()
print(result)
