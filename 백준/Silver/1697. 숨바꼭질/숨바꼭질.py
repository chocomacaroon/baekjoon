from collections import deque

def bfs():
    visited = [False] * 100001
    q = deque()
    q.append(N)
    visited[N] = True
    depth = 0

    while q:
        for _ in range(len(q)):
            x = q.popleft()
            if x == M:
                print(depth)
                return
            for nx in (x-1,x+1,x*2):
                if 0 <= nx <= 100000 and not visited[nx]:
                    visited[nx] = True
                    q.append(nx)
        depth += 1

N, M = map(int, input().split())

bfs()