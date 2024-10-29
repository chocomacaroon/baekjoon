n = int(input())

for _ in range(n):
    score = list(map(int, input().split()))
    sum_ = sum(score[1:])
    avg = sum_/score[0]
    percent = len([i for i in score[1:] if i > avg])/score[0]*100
    print("{:.3f}%".format(percent))
