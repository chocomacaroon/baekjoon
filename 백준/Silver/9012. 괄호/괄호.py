import sys
input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    stack = []
    s = input().strip()
    for c in s:
        if c == ")" and len(stack) and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(c)
    if len(stack)==0:
        print("YES")
    else:
        print("NO")