from collections import deque

def solution(maps):
    answer = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    v = [[0]*len(maps[0]) for _ in range(len(maps))]
    q = deque()
    q.append((0,0))
    v[0][0] = 1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if v[nx][ny]==0 and maps[nx][ny]==1:
                    q.append((nx,ny))
                    v[nx][ny] = v[x][y]+1
                    if nx == len(maps)-1 and ny == len(maps[0])-1:
                        return v[nx][ny]
    return -1
