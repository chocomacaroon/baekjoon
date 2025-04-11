def solution(prices):
    answer = []
    stk = []
    period = [len(prices)-i-1 for i in range(len(prices))]
    for i,c in enumerate(prices):
        if stk and stk[-1][1] > c:
            while stk and stk[-1][1] > c:
                ii,cc = stk.pop()
                period[ii] = i-ii
        stk.append((i,c))
    return period