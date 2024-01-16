S = input()
max
max_cnt = 0
alph = [0 for _ in range(26)]
for i in S:
  alph[ord(i.upper())-ord('A')] += 1
if alph.count(max(alph))>1: 
  print('?')
else:
  print(chr(ord('A')+alph.index(max(alph))))