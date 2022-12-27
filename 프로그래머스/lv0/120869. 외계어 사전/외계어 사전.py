from itertools import permutations
def solution(spell, dic):
    dic = [i for i in dic if len(i) == len(spell)]
    permutation = ["".join(i) for i in permutations(spell, len(spell))]
    
    for i in permutation:
        if i in dic:
            return 1
    return 2