def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a

n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    print(a*b//gcd(a,b))


