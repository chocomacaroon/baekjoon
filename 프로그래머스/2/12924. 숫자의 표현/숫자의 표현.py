def solution(n):
    answer = 0
    su = 0
    for i in range(n+1):
        start = i+1
        for j in range(start,n+1):
            su += j
            if su > n:
                su = 0
                break
            elif su == n:
                answer+=1
                su = 0
                break
    return answer