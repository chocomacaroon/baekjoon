N = int(input())
num = []
for _ in range(N):
  num.append(int(input()))
num.sort()
print(*num, sep='\n')