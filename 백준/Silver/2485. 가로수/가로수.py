import math

n = int(input())

lst = []
dif = []

for i in range(n):
  num = int(input())
  lst.append(num)

for i in range(1,len(lst)):
  dif.append(lst[i]-lst[i-1])

d = dif[0]

for n in dif:
  d = math.gcd(d,n)

answer = 0

for n in dif:
  if n > d:
    answer += (n // d-1)
print(answer)