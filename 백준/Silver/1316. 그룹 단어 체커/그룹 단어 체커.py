n = int(input())
words = []
alph = []
cnt = 0
for i in range(n):
  words.append(input())
for _ in words:
  for j in range(len(_)):
    if (_[j] in alph) == True:
      if _[j-1] != _[j]:
        alph = []
        break
    if (_[j] in alph) == False:
      alph.append(_[j])
  if alph:
    cnt+=1
  alph = []
print(cnt)