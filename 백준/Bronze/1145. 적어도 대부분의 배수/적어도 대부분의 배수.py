num = list(map(int,input().split()))
i = 1
cnt = 0
while True:
  i+=1
  for j in range(5):
    if i % num[j] == 0:
      cnt+=1
    if cnt == 3:
      print(i)
      break
  if cnt == 3:
    break
  cnt = 0