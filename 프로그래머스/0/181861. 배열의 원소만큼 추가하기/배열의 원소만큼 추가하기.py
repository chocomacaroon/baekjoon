def solution(arr):
    answer = []
    for i in arr:
        for  n in range(i):
            answer.append(i)
    return answer