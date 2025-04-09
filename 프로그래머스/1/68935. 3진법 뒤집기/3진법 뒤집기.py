def solution(n):
    answer = 0
    n3 = ""
    while n//3>0:
        n3 += str(n%3)
        n //= 3
    n3 += str(n%3)
    n3 = n3[::-1]
    rev = str(int(n3))
    for i,c in enumerate(rev):
        answer += int(c)*(3**i)
    return answer