import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
queue = deque()

for _ in range(N):
    s = input().strip()
    if s == "pop":
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif s == "size":
        print(len(queue))
    elif s == "empty":
        if len(queue):
            print(0)
        else:
            print(1)
    elif s == "front":
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif s == "back":
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
    else:
        _,x = s.split()
        queue.append(int(x))