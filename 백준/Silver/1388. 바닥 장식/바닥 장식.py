import sys
input = sys.stdin.readline

n,m = map(int,input().strip().split())
cnt = 0
stack = []
for _ in range(n):
    s = input().strip()
    tmp = []
    for c in s:
        if (len(tmp) and tmp[-1] == "|" and c == "-") or (c=="-" and len(tmp)==0):
            cnt+=1
        tmp.append(c)
    stack.append(tmp)

for i in range(m):
    tmp = []
    for j in range(n):
        c = stack[j][i]
        if (len(tmp) and tmp[-1] == "-" and c == "|") or (c=="|" and len(tmp)==0):
            cnt+=1
        tmp.append(c)
    stack.append(tmp)
print(cnt)