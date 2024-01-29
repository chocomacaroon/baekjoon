A = int(input())
for i in range(A):
  num = list(map(int, input().split()))
  num.sort(reverse=True)
  print(num[2])
  num = []