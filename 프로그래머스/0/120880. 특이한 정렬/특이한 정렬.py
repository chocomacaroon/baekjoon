def solution(numlist, n):
    answer = []
    tmp = []
    numlist.sort(reverse=True)
    for c in numlist:
        tmp.append(abs(c-n))
    sort = sorted(tmp)
    for a in sort:
        answer.append(numlist[tmp.index(a)])
        tmp[tmp.index(a)] = -1
    return answer