def second_largest_number(lst):
    if len(lst):
        max_ = float('-inf')
        less = float('-inf')
        for i in lst:
            if i > max_:
                less = max_
                max_ = i
            elif i > less:
                less = i
        return less
    else:
        return None


lst_ = [-150, 4, 2, 1, 5, 2, 5,  7]
print(second_largest_number(lst_))
