def solution(num_list):
    answer = []
    odd_cnt = 0
    even_cnt = 0
    for n in num_list:
        if n % 2:
            odd_cnt += 1
        else:
            even_cnt += 1
    answer = [even_cnt, odd_cnt]
    return answer