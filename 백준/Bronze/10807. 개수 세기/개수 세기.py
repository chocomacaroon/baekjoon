N = int(input())
array = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in array:
  if v == i:
    cnt+=1
print(cnt)