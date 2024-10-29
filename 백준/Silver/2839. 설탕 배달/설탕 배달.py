N = int(input())
three = 0
five = 0

while True:
    if N%5==0:
        five=N//5
        print(three+five)
        break
    else:
        N -= 3
        three+=1
    if N < 0:
        print(-1)
        break