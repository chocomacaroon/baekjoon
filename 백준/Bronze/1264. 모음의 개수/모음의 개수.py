moem = ['a', 'e', 'i', 'o', 'u']
while True:
  cnt = 0
  S = input()
  if S == "#": break;
  for i in S:
      if i.lower() in moem:
        cnt += 1
  print(cnt)