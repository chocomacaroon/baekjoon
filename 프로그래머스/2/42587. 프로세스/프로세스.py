def solution(priorities, location):
    answer = 0
    q = []
    sequence = []
    idx = 0
    for i, p in enumerate(priorities):
        q.append([i,p])
    
    while q:
        flag = True
        idx, p = q.pop(0)
        for i,x in q:
            if x > p:
                q.append([idx,p])
                flag = False
                break
        if flag:
            sequence.append(idx)
    return sequence.index(location)+1