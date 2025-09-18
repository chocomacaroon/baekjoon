def solution(name, yearning, photo):
    answer = []
    for p in photo:
        su = 0
        for n in p:
            if n in name:
                su += yearning[name.index(n)]
        answer.append(su)
    return answer