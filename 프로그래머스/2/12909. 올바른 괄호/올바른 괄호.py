def solution(s):
    stk = []
    for c in s:
        if c == ')':
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(c)
        elif c == '(':
            stk.append(c)
    return False if stk else True