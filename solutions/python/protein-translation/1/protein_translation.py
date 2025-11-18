def proteins(strand):
    strand_len = len(strand)
    res = []
    genetic_code = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine", "UUG": "Leucine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "UAU": "Tyrosine", "UAC": "Tyrosine",
    "UGU": "Cysteine", "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }
    for i in range(strand_len):
        Aminoacid = strand[i*3:(i+1)*3]
        if genetic_code.get(Aminoacid) is None:
            break
        if Aminoacid == '' or genetic_code[Aminoacid] == 'STOP':
            break
        res.append(genetic_code[Aminoacid])
    return res
    
print(proteins('AUGUUUUGGCCCUGA'))