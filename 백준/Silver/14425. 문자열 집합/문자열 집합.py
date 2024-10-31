import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())
store = set()
for _ in range(N):
    store.add(input().strip())

cnt = 0

for _ in range(M):
    c = input().strip()
    if c in store:
        cnt+=1
print(cnt)