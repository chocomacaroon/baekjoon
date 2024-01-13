N, M = map(int, input().split())
numbers = [i+1 for i in range(0, N)]
for i in range(M):
  i, j = map(int, input().split())
  for n in range(i, (i+j)//2+1):
    numbers[n-1], numbers[j+i-n-1] = numbers[j+i-n-1], numbers[n-1]
print(*numbers)