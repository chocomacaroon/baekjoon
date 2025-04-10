def solution(k, dungeons):
    answer = -1
    v = [0]*len(dungeons)
    lst = []
    def dfs(tmp,n):
        if n == len(dungeons):
            lst.append(tmp[:])
            return
        for i in range(len(dungeons)):
            if v[i]==0:
                v[i]=1
                tmp.append(dungeons[i])
                dfs(tmp,n+1)
                tmp.pop()
                v[i]=0
    
    dfs([],0)
    cntlst = []
    for dun in lst:
        nk = k
        cnt = 0
        for x,y in dun:
            if nk >= x:
                cnt+=1
                nk-=y
            else:
                break
        cntlst.append(cnt)
    return max(cntlst)

