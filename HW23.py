lst = [1, 2, 3, 4, 5, 6]


def to_dict(lst):
    even = []
    not_even = []
    for i in range(1, len(lst) + 1):
        if i % 2 == 0:
            even.append(lst[i - 1])
        else:
            not_even.append(lst[i - 1])

    dict_ = {}
    for i, i_ in zip(not_even, even):
        dict_.update({i: i_})

    return dict_


