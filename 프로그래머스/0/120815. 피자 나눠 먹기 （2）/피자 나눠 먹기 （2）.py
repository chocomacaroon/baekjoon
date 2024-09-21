def solution(n):
    answer = 0
    for i in range(1,7):
        if n*i % 6 == 0:
            return n*i//6
    return answer