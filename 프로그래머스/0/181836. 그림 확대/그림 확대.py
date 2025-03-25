def solution(picture, k):
    answer = []
    for p in picture:
        tmp = ""
        for c in p:
            tmp += c * k
        for _ in range(k):
            answer.append(tmp)
    return answer