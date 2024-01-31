from collections import deque
N, K = map(int, input().split())
num = [i+1 for i in range(N)]
num = deque(num)
result = []
while True:
  if len(num) == 0:
    break
  num.rotate(-K+1)
  result.append(num[0])
  num.remove(num[0])
print('<',end='')
print(*result, sep=', ', end='')
print('>')