N, M = map(int, input().split())
v = [0]*(N+1)
ans = []

def dfs(n):
    if n == M:
        print(*ans)
        return
    for i in range(1,N+1):
        if v[i] == 0:
            v[i] = 1
            ans.append(i)
            dfs(n+1)
            ans.pop()
            v[i] = 0

dfs(0)