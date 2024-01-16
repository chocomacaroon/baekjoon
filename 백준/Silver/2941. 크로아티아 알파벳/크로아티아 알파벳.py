words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
S = input()
cnt = len(S)
i = 0

while i < len(S):
  for _ in words:
    if S[i:].find(_) == 0:
      cnt -= (len(_)-1)
      i+= (len(_)-1)
      break
  i+=1
print(cnt)