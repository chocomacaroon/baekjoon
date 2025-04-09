def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(1,count+1):
        total += price*i
        print(price*i)
    return total-money if money < total else 0