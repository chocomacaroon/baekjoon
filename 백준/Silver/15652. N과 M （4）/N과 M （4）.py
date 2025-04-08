N, M = map(int, input().split())

result = []
ans = []

def dfs(start, n):
    if n == M:
        result.append(ans[:])
        return
    for i in range(start,N+1):
        ans.append(i)
        dfs(i, n+1)
        ans.pop()

dfs(1,0)
for s in result:
    print(*s)