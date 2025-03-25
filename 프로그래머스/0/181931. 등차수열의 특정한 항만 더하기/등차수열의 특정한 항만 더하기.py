def solution(a, d, included):
    answer = 0
    lst = [i for i in range(a,a+len(included)*d+1,d)]
    for i,b in enumerate(included):
        if b:
            answer += lst[i]
    return answer