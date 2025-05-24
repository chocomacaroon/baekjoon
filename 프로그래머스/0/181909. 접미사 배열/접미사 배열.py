def solution(my_string):
    answer = []
    tmp = ""
    for c in my_string[::-1]:
        tmp = c + tmp
        answer.append(tmp)
    return sorted(answer)