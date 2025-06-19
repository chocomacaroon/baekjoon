N = int(input())

m = []
v = [[False] * N for _ in range(N)]
result = []
cnt = 0

for _ in range(N):
    m.append(list(map(int,list(input()))))

def dfs(v,m,x,y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    v[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 1 and not v[nx][ny]:
            cnt += 1
            dfs(v, m, nx, ny)

for i in range(N):
    for j in range(N):
        if m[i][j] == 1 and not v[i][j]:
            cnt = 1
            dfs(v,m,i,j)
            result.append(cnt)
print(len(result))
print(*sorted(result),sep = "\n")