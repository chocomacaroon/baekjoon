import sys

input = sys.stdin.readline

N = int(input().strip())
queue = []

for _ in range(N):
    c = input().strip()
    if c == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif c == "size":
        print(len(queue))
    elif c == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif c == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif c == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        _,x = c.split()
        queue.append(x)
