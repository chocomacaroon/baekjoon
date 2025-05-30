import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N)]
v = [False] * N

for _ in range(M):
    s,e = map(int,sys.stdin.readline().split())
    graph[s-1].append(e-1)
    graph[e-1].append(s-1)

answer = 0
# print(*graph,sep = '\n')

q = deque()
q.append(0)
v[0] = True
while q:
    x = q.pop()
    for y in graph[x]:
        if not v[y]:
            v[y] = True
            answer += 1
            q.append(y)

print(answer)