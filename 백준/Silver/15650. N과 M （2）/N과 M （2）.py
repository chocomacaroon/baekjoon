N,M = map(int, input().split())
v = [0]*(N+1)
result = []
ans = []

def dfs(n,start):
    if n == M:
        result.append(ans[:])
        return
    for i in range(start+1,N+1):
        if v[i] == 0:
            v[i] = 1
            ans.append(i)
            dfs(n+1,i)
            v[i] = 0
            ans.pop()

dfs(0,0)

for i in result:
    print(*i,sep=' ')