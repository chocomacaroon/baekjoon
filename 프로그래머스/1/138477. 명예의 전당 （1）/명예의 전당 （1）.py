def solution(k, score):
    answer = []
    stk = []
    for n in score:
        if len(stk) < k:
            stk.append(n)
            stk.sort(reverse=True)
            answer.append(stk[-1])
        else:
            stk.append(n)
            stk.sort(reverse=True)
            stk = stk[:k]
            answer.append(stk[-1])
    return answer