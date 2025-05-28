T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    ql = []
    for i in range(len(q)):
        ql.append([i,q[i]])
    cnt = 0
    while ql:
        if ql[0] == max(ql, key=lambda x:x[1]): #1들중
            if ql[0][0] == M:
                ql.pop(0)
                break
            else:
                ql.pop(0)
            cnt += 1
        else:
            c = ql[0]
            ql.pop(0)
            ql.append(c)
    print(cnt+1)