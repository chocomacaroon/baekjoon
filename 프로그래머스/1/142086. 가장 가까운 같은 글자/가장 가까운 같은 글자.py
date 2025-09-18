def solution(s):
    answer = []
    tmp = []
    for c in s:
        if c not in tmp:
            answer.append(-1)
        else:
            answer.append(tmp[::-1].index(c)+1)
        tmp.append(c)
    return answer