def solution(n):
    answer = 0
    if n <= 1:
        return n
    else:
        f0 = 0
        f1 = 1
        for i in range(2,n+1):
            f0,f1 = f1,f0+f1
        return f1%1234567