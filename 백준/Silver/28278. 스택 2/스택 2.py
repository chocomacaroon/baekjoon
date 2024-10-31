import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())
stack = []

for _ in range(N):
    s = input().strip()
    if s == "2":
        if len(stack):
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    elif s == "3":
        print(len(stack))
    elif s == "4":
        if len(stack):
            print(0)
        else:
            print(1)
    elif s == "5":
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    else:
        _,x = s.split()
        stack.append(int(x))