def solution(s):
    stk = []
    for c in s:
        if not stk:
            stk.append(c)
        else:
            if stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
    if stk:
        return 0
    else:
        return 1