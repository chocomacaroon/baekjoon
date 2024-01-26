N = int(input())
S = set()
for _ in range(N):
  S.add(input())
S = sorted(list(S))
S = sorted(S, key=len)
print(*S, sep = '\n')