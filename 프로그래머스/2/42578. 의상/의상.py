def solution(clothes):
    answer = 1
    dic = dict()
    for v,k in clothes:
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
    for n in dic.values():
        answer*=(n+1)
    return answer-1