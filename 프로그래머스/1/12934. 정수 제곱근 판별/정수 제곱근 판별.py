def solution(n):
    answer = 0
    if n == (int(n**0.5))**2:
        return (int(n**0.5)+1)**2
    else:
        return -1
    return answer