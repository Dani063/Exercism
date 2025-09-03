def to_rna(dna_strand):
    sol = ""
    conversor = dict({'A':'U','G':'C','C':'G','T':'A'})
    for letter in dna_strand:
        if letter in conversor.keys():
            sol += conversor[letter]
    return sol