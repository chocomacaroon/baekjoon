T = int(input())

def dfs(n, res):
    global cnt
    if res > n:
        return
    if res == n:
        cnt += 1
        return
    num = [1,2,3]
    for i in num:
        dfs(n, res + i)

for _ in range(T):
    cnt = 0
    n = int(input())
    dfs(n, 0)
    print(cnt)
