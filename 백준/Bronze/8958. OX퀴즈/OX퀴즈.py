N = int(input())
score = 0
total_score = 0
for _ in range(N):
  S = list(input())
  for i in S:
    if(i == 'O'):
      score += 1
    else:
      score = 0
    total_score  += score
  print(total_score)
  score = 0
  total_score = 0