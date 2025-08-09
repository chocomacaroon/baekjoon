from collections import deque

def solution(maps):
    
    visited = [[False]*len(maps[0]) for i in range(len(maps))]
    visited[0][0] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    
    q = deque()
    q.append((0,0, 1))
    
    while q:
        nx, ny, dis = q.popleft()
        if nx == len(maps)-1 and ny == len(maps[0])-1:
            return dis
        for i in range(4):
            if nx + dx[i] >= 0 and nx + dx[i] < len(maps) and ny + dy[i] >= 0 and ny + dy[i] < len(maps[0]):
                if maps[nx + dx[i]][ny + dy[i]] == 1 and not visited[nx + dx[i]][ny + dy[i]]:
                    visited[nx + dx[i]][ny + dy[i]] = True
                    q.append((nx + dx[i],ny + dy[i], dis+1))

    return -1