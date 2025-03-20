def solution(balls, share):
    answer = 0
    return factorial(balls)//(factorial(share)*factorial(balls-share))
    return answer

def factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer