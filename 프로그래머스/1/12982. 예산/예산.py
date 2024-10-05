def solution(d, budget):
    max = 0
    d.sort()
    for i in range(len(d)+1):
        for j in range(i+1,len(d)+1):
            if sum(d[i:j]) <= budget:
                if len(d[i:j])>=max:
                    max = len(d[i:j])
    return max