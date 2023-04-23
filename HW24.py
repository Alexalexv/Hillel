lst = [12, 10, 9, 11, 2, 1, 5, 2, 5, 7, -1]


def second_largest_number(lst):
    maxi = None
    less = None

    for i in lst:
        if maxi is None or i > maxi:
            less = maxi
            maxi = i
        elif less is None or i > less:
            less = i
    return less
