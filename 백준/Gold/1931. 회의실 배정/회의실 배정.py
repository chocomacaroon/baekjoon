N = int(input())

lst = []

for _ in range(N):
    s,e = map(int,input().split())
    lst.append((s,e))

lst.sort(key=lambda x:(x[1],x[0]))
cnt = 0
be = 0

for s,e in lst:
    if s >= be:
        cnt+=1
        be = e

print(cnt)