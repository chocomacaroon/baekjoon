def solution(price):
    answer = price
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price
    answer //= 1
    return answer