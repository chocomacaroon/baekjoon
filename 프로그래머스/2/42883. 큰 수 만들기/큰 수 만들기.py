def solution(number, k):
    stk = []
    for c in number:
        while stk and k > 0 and stk[-1] < c:
            stk.pop()
            k -= 1
        stk.append(c)
    if k > 0:
        stk = stk[:-k]
    return ''.join(stk)