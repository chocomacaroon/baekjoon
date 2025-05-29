
ans = []

def dfs(l,answer,pos):
    global ans
    if len(answer) == 7:
        if sum(answer) == 100:
            ans = answer
        return
    if sum(answer) > 100 or pos == len(l):
        return
    dfs(l, answer + [l[pos]], pos+1)
    dfs(l,answer, pos+1)

lst = []

for i in range(9):
    lst.append(int(input()))

dfs(lst,[], 0)

print(*ans,sep="\n")