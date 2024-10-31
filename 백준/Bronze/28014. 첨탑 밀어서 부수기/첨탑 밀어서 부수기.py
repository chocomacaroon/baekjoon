n = int(input())
top = list(map(int, input().split()))
cnt = 0
height = 0

for t in top:
    if t >= height:
        cnt+=1
        height = t
    else:
        height = t
        pass
print(cnt)