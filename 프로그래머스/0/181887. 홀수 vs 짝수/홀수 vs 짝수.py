def solution(num_list):
    sum_even = sum([i for i in num_list[::2]])
    sum_odd = sum([i for i in num_list[1::2]])
    return sum_even if sum_even > sum_odd else sum_odd