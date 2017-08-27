from collections import defaultdict


def to_rna(dna):
    for letter in dna:
        if letter not in "GCTA":
            return ""
    dic = defaultdict(str)
    dic.update({ord('G'): 'C', ord('C'): 'G', ord('T'): 'A', ord('A'): 'U'})
    return dna.translate(dic)
