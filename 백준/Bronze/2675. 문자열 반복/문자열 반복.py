T = int(input())
for _ in range(T):
  N, S = input().split()
  for i in S:
    print(i*int(N), end="")
  print()