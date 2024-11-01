import sys
input = sys.stdin.readline

n = int(input().strip())
a = 1
b = 2
line = 1
i = 0
tmp=1
while True:
    i += 1
    tmp+=i
    if tmp > n:
        break
line = i
# print(line)
# print(i, n-tmp+i+1) #i번째줄 n-tmp+i+1번
if i%2:
    print(f"{i-(n-tmp+i+1)+1}/{(n-tmp+i+1)}")
else:
    print(f"{(n - tmp + i + 1)}/{i - (n - tmp + i + 1) + 1}")
# 1 1
# 2 2 3
# 3
#
# 1 / 2 3 / 4 5 6 / 7 8 9 10 /

