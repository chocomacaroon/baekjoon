import sys
input = sys.stdin.readline

N,K = map(int, input().strip().split())
coin = []
for _ in range(N):
    n = int(input().strip())
    coin.append(n)
i = 0
cnt=0
coin = coin[::-1]
while K > 0:
    if K//coin[i]:
        cnt += K//coin[i]
        K %= coin[i]
        i+=1
    else:
        i+=1

print(cnt)