import sys

input = sys.stdin.readline
stack = []
N = int(input().strip())

for _ in range(N):
    s = input().strip()
    if s == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif s == "size":
        print(len(stack))
    elif s == "empty":
        print(int(bool(not len(stack))))
    elif s == "top":
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    else:
        com, n = s.split()
        n = int(n)
        if com == "push":
            stack.append(n)