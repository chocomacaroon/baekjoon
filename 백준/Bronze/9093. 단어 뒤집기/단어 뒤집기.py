T = int(input())
for i in range(T):
  S = input().split()
  for i in S:
    print(i[::-1], end=' ')
  print()