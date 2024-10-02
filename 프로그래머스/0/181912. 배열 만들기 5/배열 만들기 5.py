def solution(intStrs, k, s, l):
    answer = []
    for n in intStrs:
        tmp = int(n[s:s+l])
        if tmp>k:
            answer.append(tmp)
    return answer