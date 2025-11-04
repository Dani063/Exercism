SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST
    if len(list_one) > len(list_two):
        if is_sublist(list_two, list_one):
            return SUPERLIST
    if len(list_two) > len(list_one):
        if is_sublist(list_one, list_two):
            return SUBLIST
    return UNEQUAL


def is_sublist(small, large):
    i = 0
    j = 0

    while i < len(large):
        if large[i] == small[j]:
            j += 1
            i += 1
            if j == len(small):
                return True
        else:
            i = i - j + 1
            j = 0
    return False
