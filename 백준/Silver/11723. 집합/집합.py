import sys
N = int(input())
S = set()
for _ in range(N):
    m = sys.stdin.readline().strip()
    if m == "all":
        S = set([i for i in range(1, 21)])
    elif m == "empty":
        S = set()
    else:
        com, x = m.split()
        x = int(x)
        if com == "add":
            S.add(x)
        elif com == "remove":
            S.discard(x)
        elif com == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif com == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)