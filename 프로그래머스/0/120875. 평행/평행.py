def solution(dots):
    answer = 0
    x1,y1 = dots[0]
    x2,y2 = dots[1]
    x3,y3 = dots[2]
    x4,y4 = dots[3]
    if (y1-y2)/(x1-x2) == (y3-y4)/(x3-x4):
        return 1
    if (y1-y3)/(x1-x3) == (y2-y4)/(x2-x4):
        return 1
    if (y1-y4)/(x1-x4) == (y2-y3)/(x2-x3):
        return 1
    return answer