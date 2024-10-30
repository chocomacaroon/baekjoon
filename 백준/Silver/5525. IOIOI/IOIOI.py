import sys

input = sys.stdin.readline
stamp = "OI"

N = int(input().strip())
M = int(input().strip())
S = input().strip()
P = "I"+stamp*N
cnt = 0

for i in range(M-len(P)+1):
    if S[i:i+len(P)] == P:
        cnt+=1
print(cnt)