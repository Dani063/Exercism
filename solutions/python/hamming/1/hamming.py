def distance(strand_a, strand_b):
    cont = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for index in range(0,len(strand_a)):
        if strand_a[index] != strand_b[index]:
            cont += 1
    return cont