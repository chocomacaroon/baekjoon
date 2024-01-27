def is_prime(i):
  if i == 1:
     return False
  for j in range(2, i):
    if i % j == 0:
       return False
  return True
num = []
M = int(input())
N = int(input())
for i in range(M, N+1):
    if is_prime(i):
       num.append(i)
if num:
  print(sum(num))
  print(min(num))
else:
   print(-1)