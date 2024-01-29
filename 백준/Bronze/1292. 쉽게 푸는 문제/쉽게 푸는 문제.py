A, B = map(int, input().split())
sum = 0
cnt = 0
n = 1
while True:
  if cnt == B:
    break
  for i in range(n):
    cnt+=1
    if cnt >= A and cnt <= B:
      sum += n
    if cnt == B:
      break
  n+=1
print(sum)