max = 0
for i in range(1, 6):
  a, b, c, d = map(int, input().split())
  if a+b+c+d > max: 
    max = a+b+c+d
    winner = i
if winner:
  print(winner, max)