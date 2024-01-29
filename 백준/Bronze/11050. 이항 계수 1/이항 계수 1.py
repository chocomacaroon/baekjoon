N, K = map(int, input().split())
result = 1
if K == 0:
    print(1)
else:
  for i in range(0, K):
    result *= (N-i)
  for i in range(1, K+1):
    result //= i
  print(result)