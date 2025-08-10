from collections import deque

def solution(maps):
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    
    length = 1
    q = deque()
    q.append((0, 0, length))
    visited[0][0] = True
    
    ans = []
    while q:
        x,y,length = q.popleft()
        if x == len(maps)-1 and y == len(maps[0])-1:
            return length
        for i in range(4):
            if x+dx[i] >=0 and x+dx[i] < len(maps) and y+dy[i] >= 0 and y+dy[i] < len(maps[0]):
                if not visited[x+dx[i]][y+dy[i]] and maps[x+dx[i]][y+dy[i]] == 1:
                    visited[x+dx[i]][y+dy[i]] = True
                    q.append((x+dx[i], y+dy[i], length+1))
    return -1