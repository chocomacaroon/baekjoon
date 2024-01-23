sum = 0
min = float('inf')
for i in range(7):
  N = int(input())
  if N%2==1:
    sum += N
    if N < min: min = N
if sum == 0:
  print(-1)
else:
  print(sum)
  print(min)