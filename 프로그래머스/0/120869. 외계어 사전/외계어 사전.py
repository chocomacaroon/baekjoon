import itertools

def solution(spell, dic):
    answer = 0
    comb = itertools.permutations(spell,len(spell))
    for s in comb:
        if "".join(s) in dic:
            return 1
    return 2