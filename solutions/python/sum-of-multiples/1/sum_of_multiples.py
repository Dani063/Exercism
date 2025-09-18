def sum_of_multiples(limit, multiples):
    multiples_list = []
    for mult in multiples:
        if mult <= 0:
            continue
        count = 1
        while mult * count < limit:
            multiples_list.append(mult * count)
            count += 1
    return sum(set(multiples_list))