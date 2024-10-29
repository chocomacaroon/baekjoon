def combination(n,r):
    return fact(n)//(fact(r)*fact(n-r))

def fact(n):
    result = 1
    if n == 1:
        return 1
    for i in range(1,n+1):
        result*=i
    return result

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(combination(M,N))