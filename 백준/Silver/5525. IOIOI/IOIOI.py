import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
S = input().strip()

cnt = 0
cur = 0
result = 0

while cur < (M-1):
    if S[cur:cur+3] == "IOI":
        cnt += 1
        cur += 2
        if cnt == N:
            result += 1
            cnt -= 1
    else:
        cnt = 0
        cur += 1

print(result)