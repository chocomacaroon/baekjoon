N, M = map(int, input().split())
balls = [i+1 for i in range(N)]
for a in range(M):
  i, j = map(int, input().split())
  balls[i-1], balls[j-1] = balls[j-1], balls[i-1]
for c in range(N):
  print(balls[c], end=' ')