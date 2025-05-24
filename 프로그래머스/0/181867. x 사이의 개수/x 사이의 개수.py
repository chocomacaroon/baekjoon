def solution(myString):
    answer = []
    lst = myString.split('x')
    for s in lst:
        answer.append(len(s))
    return answer