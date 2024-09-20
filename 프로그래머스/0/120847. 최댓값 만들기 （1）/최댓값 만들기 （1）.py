def solution(numbers):
    answer = 0
    m = max(numbers)
    numbers.remove(m)
    return m * max(numbers)
    return answer