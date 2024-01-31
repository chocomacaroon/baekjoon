from collections import deque
import sys
N = int(input())
D = deque()
for i in range(N):
    s = sys.stdin.readline().rstrip()
    if s[0:10] == 'push_front':
        D.appendleft(int(s[11:]))
    if s[0:9] == 'push_back':
        D.append(int(s[10:]))
    if s == 'pop_front':
        if D:
            print(D.popleft())
        else:
            print(-1)
    if s == 'pop_back':
        if D:
            print(D.pop())
        else:
            print(-1)
    if s == 'size':
        print(len(D))
    if s == 'empty':
        if D:
            print(0)
        else:
            print(1)
    if s == 'front':
        if D:
          print(D[0])
        else:
            print(-1)
    if s == 'back':
        if D:
          print(D[-1])
        else:
            print(-1)