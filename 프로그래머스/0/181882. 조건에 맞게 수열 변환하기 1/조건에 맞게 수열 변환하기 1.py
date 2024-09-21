def solution(arr):
    answer = []
    for c in arr:
        if c >=50 and c%2==0:
            answer.append(c//2)
        elif c < 50 and c%2:
            answer.append(c*2)
        else: answer.append(c)
    return answer