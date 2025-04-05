from collections import deque

N, M = map(int, input().split())
mp = []
visited = []
for _ in range(N):
    mp.append(list(input()))
    visited.append([False for _ in range(M)])

def bsf(mp,x,y,visited):
    answer = 0
    q = deque()
    q.append([x,y])
    flag = False
    while q:
        answer+=1
        tmp = []
        while q:
            x, y = q.popleft()
            if x == N-1 and y == M-1:
                flag = True
                break

            if x+1 < N and mp[x+1][y] == '1' and not visited[x+1][y]:
                tmp.append([x+1,y])
                visited[x+1][y] = True
            if y+1 < M and mp[x][y+1] == '1' and not visited[x][y+1]:
                tmp.append([x,y+1])
                visited[x][y+1] = True
            if y-1 >= 0 and mp[x][y-1] == '1' and not visited[x][y-1]:
                tmp.append([x,y-1])
                visited[x][y-1] = True
            if x-1 >= 0 and mp[x-1][y] == '1' and not visited[x-1][y]:
                tmp.append([x-1,y])
                visited[x-1][y] = True
        q.extend(tmp)
        if flag:
            break
    print(answer)

bsf(mp,0,0,visited)