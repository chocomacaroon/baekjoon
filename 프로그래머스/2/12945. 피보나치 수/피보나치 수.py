def solution(n):
    n1 = 0
    n2 = 1
    if n == 0 : return 0
    if n == 1 : return 1
    for i in range(2, n+1):
        n1, n2 = n2, n1 + n2
    return n2 % 1234567