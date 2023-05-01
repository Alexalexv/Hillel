lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]


def linearize_list(lst, lst_=None):
    if not lst_:
        lst_ = []
    for i in lst:
        if isinstance(i, list):
            linearize_list(i, lst_)
        else:
            lst_.append(i)
    return lst_


print(linearize_list(lst))
