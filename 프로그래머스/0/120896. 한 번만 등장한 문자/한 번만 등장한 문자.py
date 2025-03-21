def solution(s):
    answer = ''
    se = set()
    remove = set()
    for c in s:
        if c in se:
            remove.add(c)
        else:
            se.add(c)
    se = se - remove
    answer = "".join(sorted(list(se)))
    return answer