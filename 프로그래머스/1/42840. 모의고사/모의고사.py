def solution(answers):
    answer = []
    one = [1,2,3,4,5]*(len(answers)//5+1)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8+1)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10+1)
    ones = 0
    twos = 0
    threes = 0
    for i,n in enumerate(answers):
        if n == one[i]:
            ones+=1
        if n == two[i]:
            twos+=1
        if n == three[i]:
            threes+=1
    sc = [ones, twos, threes]
    ma = max(sc)
    for i in range(len(sc)):
        if sc[i] == ma:
            answer.append(i+1)
    return answer