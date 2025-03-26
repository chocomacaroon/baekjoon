def solution(dots):
    answer = 0
    wid = set()
    hig = set()
    for w,h in dots:
        wid.add(w)
        hig.add(h)
    answer = abs(list(wid)[0]-list(wid)[1]) * abs(list(hig)[0]-list(hig)[1])
    return answer