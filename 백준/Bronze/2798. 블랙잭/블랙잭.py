N, M = map(int, input().split())
card = list(map(int, input().split()))
sum = []
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum.append(card[i]+card[j]+card[k])
sum.sort()
key = -1
for a in sum:
    if a > M:
        key = sum.index(a)
        break
if key == -1:
    print(sum[-1])
else:    
  print(sum[key-1])