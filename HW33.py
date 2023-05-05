import copy


def custom_zip(*sequences, full=False, default=None):
    sequences_ = copy.deepcopy(sequences)

    if full:
        len_ = len(max(sequences_, key=len))
        for i in sequences_:
            len_element = len(i)
            if len_element != len_:
                diff_len = len_ - len_element
                a = 0
                while a < diff_len:
                    i.append(default)
                    a += 1

    else:
        len_ = len(min(sequences_, key=len))
        for i in sequences_:
            len_element = len(i)
            if len_element != len_:
                del i[len_:]

    result = []
    i = 0
    while i < len_:
        tuple_ = tuple()
        for a in sequences_:
            tuple_ += (a[i],)
        result.append(tuple_)
        i += 1
    return result


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

print(custom_zip(seq1, seq2))
print(custom_zip(seq1, seq2, full=True, default="Q"))
