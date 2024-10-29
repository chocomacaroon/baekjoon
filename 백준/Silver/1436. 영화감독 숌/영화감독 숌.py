N = int(input())

six = "666"

i = 1
cnt = 0

while True:
    if six in str(i):
        cnt+=1
        if cnt == N:
            print(i)
            break
    i+=1