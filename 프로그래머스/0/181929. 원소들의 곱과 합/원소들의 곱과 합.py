def solution(num_list):
    sub = 1
    for n in num_list:
        sub *= n
    return int(sum(num_list)**2 > sub)