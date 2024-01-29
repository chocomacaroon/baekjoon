x, y = map(int, input().split())
for i in range(max(x,y), 0, -1):
    if x % i == 0 and y % i == 0:
        print(i)
        break
num = max(x, y)
a = x
b = y
i = j = 1
while True:
    if a < b:
      a = x * i
      i += 1
    elif a > b:
      b = y * j
      j += 1
    if a == b:
        print(a)
        break