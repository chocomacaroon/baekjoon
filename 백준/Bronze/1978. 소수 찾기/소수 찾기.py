def is_prime(i):
  if i == 1:
     return False
  for j in range(2, i):
    if i % j == 0:
       return False
  return True

N = int(input())
cnt = 0
num = list(map(int, input().split()))
for i in num:
    if is_prime(i):
        cnt+=1
print(cnt)