N,M = map(int, input().split())
v = [0]*(N+1)
result = []
ans = []

def dfs(n):
    if n == M:
        result.append(ans[:])
        return
    for i in range(1,N+1):
        ans.append(i)
        dfs(n+1)
        v[i] = 0
        ans.pop()

dfs(0)

for i in result:
    print(*i,sep=' ')