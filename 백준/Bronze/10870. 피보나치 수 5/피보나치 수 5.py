def FIBO(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return FIBO(N-2) + FIBO(N-1)
    
n = int(input())
print(FIBO(n))