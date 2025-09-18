def solution(sizes):
    answer = 0
    big = max(sizes[0])
    small = min(sizes[0])
    
    for a,b in sizes:
        if a>b:
            if a > big:
                big = a
            if b > small:
                small = b
        else:
            if b > big:
                big = b
            if a > small:
                small = a
    return small*big