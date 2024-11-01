import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

deck = deque()

for _ in range(n):
    s = input().strip()
    if s == "3":
        if len(deck):
            print(deck.popleft())
        else:
            print(-1)
    elif s == "4":
        if len(deck):
            print(deck.pop())
        else:
            print(-1)
    elif s == "5":
        print(len(deck))
    elif s == "6":
        if len(deck):
            print(0)
        else:
            print(1)
    elif s == "7":
        if len(deck):
            print(deck[0])
        else:
            print(-1)
    elif s == "8":
        if len(deck):
            print(deck[-1])
        else:
            print(-1)
    else:
        m,x = s.split()
        x = int(x)
        if m == "1":
            deck.appendleft(x)
        if m == "2":
            deck.append(x)