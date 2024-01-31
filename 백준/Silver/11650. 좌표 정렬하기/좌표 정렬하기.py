N = int(input())
xy = []
for i in range(N):
    xy.append(list(map(int, input().split())))
xy.sort()
for i in range(N):
    print(*xy[i])