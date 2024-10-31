L,P = map(int, input().split())

num = list(map(int, input().split()))
for n in num:
    print(n-L*P,end=" ")