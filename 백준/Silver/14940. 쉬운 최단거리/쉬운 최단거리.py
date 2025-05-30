from collections import deque

n,m = map(int,input().split())

graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    if 2 in tmp:
        startx = i
        starty = tmp.index(2)

v = [[False]*m for _ in range(n)]
distance = [[-1]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


v = [[False] * m for _ in range(n)]
q = deque()
q.append((startx,starty))
v[startx][starty] = True
distance[startx][starty] = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            distance[i][j] = 0

while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:

            if not v[nx][ny] and graph[nx][ny] > 0:
                v[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx,ny))

for l in distance:
    print(*l,sep = " ")