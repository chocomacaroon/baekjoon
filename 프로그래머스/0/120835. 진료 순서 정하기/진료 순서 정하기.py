def solution(emergency):
    answer = []
    sort = sorted(emergency,reverse=True)
    for e in emergency:
        answer.append(sort.index(e)+1)
    return answer