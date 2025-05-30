import sys
from collections import deque

T = int(sys.stdin.readline())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(T):
    M,N,K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for i in range(N)]
    for _ in range(K):
        y,x = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    answer = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                answer += 1
                q = deque()
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx,ny = x+dx[k], y+dy[k]
                        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                            graph[nx][ny] = 0
                            q.append((nx,ny))
    print(answer)


