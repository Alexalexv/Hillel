multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
multi_string_splitted = multi_string.split('.')
multi_string_splitted.pop()
counter = []

for i in multi_string_splitted:
    sentence = i.lstrip()
    sentence_lst = sentence.split(' ')
    counter.append(len(sentence_lst))

print(counter)
