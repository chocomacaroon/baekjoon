def solution(s):
    answer = -1
    stk = []
    for c in s:
        if not stk or (stk and stk[-1]!=c):
            stk.append(c)
        else:
            while stk and stk[-1]==c:
                stk.pop()
    return 0 if stk else 1