def solution(my_string, s, e):
    answer = ''
    answer = my_string[:s]
    tmp = my_string[s:e+1]
    answer += tmp[::-1]
    answer += my_string[e+1:]
    return answer