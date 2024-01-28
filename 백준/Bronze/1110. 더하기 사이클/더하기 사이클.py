N = int(input())
cnt = 0
if N < 10:
  N = '0' + str(N)
else:
  N = str(N)
M = N
while True:
  M = M[1]+str(int(M[0])+int(M[1]))[-1]
  cnt += 1
  if M == N:
    break
print(cnt)