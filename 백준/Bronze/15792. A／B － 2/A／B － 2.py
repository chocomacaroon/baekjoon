n, m = map(int,input().split())
answer = 0
print(n//m,end="")
if n%m:
    print(".",end="")
    i = 0
    while n%m and i < 1000:
        n = n % m * 10
        i += 1
        print(n // m, end = "")