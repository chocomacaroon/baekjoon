N, M = map(int, input().split())
balls = [0 for i in range(N)]
for a in range(M):
  i, j, k = map(int, input().split())
  for b in range(i, j+1):
    balls[b-1] = k
for c in range(N):
  print(balls[c], end=' ')