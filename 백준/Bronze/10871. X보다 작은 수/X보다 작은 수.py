N, X = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
  if i < X:
    print(i, end=' ')