alp = [0 for i in range(26)]
S = input()
for i in S:
  alp[ord(i)-ord('a')]+=1
print(*alp)