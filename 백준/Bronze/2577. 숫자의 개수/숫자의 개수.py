a = int(input())
b = int(input())
c = int(input())

num = [0 for i in range(10)]
S = str(a*b*c)
for i in range(len(str(S))):
  num[int(S[i])] += 1
for i in range(10):
  print(num[i])