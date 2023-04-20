def second_largest_number(lst):
    if len(lst):
        max_ = lst[0]
        less = lst[0]
        for i in lst:
            if i > max_:
                less = max_
                max_ = i
        return less
    else:
        return None
