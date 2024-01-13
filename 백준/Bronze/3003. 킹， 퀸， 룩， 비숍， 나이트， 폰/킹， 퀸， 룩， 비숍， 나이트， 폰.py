num = [1, 1, 2, 2, 2, 8]
own = list(map(int, input().split()))
for i in range(6):
  print(num[i] - own[i], end=' ')