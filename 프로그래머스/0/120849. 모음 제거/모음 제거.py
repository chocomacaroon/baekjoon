def solution(my_string):
    answer = my_string
    moeum = ['a', 'e', 'i', 'o', 'u']
    for c in moeum:
        answer = answer.replace(c,'')
    return answer