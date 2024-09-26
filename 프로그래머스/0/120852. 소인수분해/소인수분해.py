def solution(n):
    answer = []
    for i in range(2,n+1):
        if is_prime(i) and n%i==0 and not i in answer:
            answer.append(i)
    return answer

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True