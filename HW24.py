lst = [1, 2, 2]


def second_largest_number(lst):
    set_ = set()
    for i in lst:
        set_.add(i)
    maxi = None
    less = None
    for i in set_:
        if maxi is None or i > maxi:
            less = maxi
            maxi = i
        elif less is None or i > less:
            less = i
    return less
