def cnt(n):
    res = 0
    for i in range(1,n+1):
        if n%i == 0:
            res += 1
    return res

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if cnt(i)%2==0:
            answer += i
        else:
            answer -= i
    return answer