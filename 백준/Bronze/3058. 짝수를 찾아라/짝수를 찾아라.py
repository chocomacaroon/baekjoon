T = int(input())
for _ in range(T):
  sum = 0
  min = float('inf')
  numbers = []
  numbers = list(map(int, input().split()))
  for i in numbers:
    if i % 2 == 0:
      sum += i
      min = min if min < i else i
  print(sum, min)