def solution(N, stages):
    sort = []
    for n in range(1,N+1):
        tmp = [i for i in stages if i>=n]
        if tmp.count(n)>0:
            sort.append([tmp.count(n)/len(tmp),n])
        else:
            sort.append([0,n])
    sort = sorted(sort,key=lambda x:(-x[0],x[1]))
    return [n for _,n in sort]