ans = []

def dfs(n, m, v, pos, lst):
    if len(lst) == m:
        ans.append(lst)
        return
    for i in range(pos, n):
        if not v[i]:
            v[i] = True
            dfs(n, m, v, i, lst + [i+1])
            v[i] = False

n, m = map(int, input().split())

v = [False] * n

dfs(n, m, v, 0, [])

for lst in ans:
    print(*lst)