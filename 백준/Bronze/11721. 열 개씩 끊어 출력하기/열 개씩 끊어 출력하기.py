S = input()
i = 0
while True:
  print(S[i*10:i*10+10])
  i+=1
  if i*10+10 >= len(S):
    print(S[i*10:len(S)+1])
    break