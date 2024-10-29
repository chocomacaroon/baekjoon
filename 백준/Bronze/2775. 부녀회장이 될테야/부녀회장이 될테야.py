T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    list = [i for i in range(1, n + 1)]
    list2 = [i for i in range(1, n + 1)]
    people = 0
    for i in range(k):
        for j in range(n):
            list2[j] = sum(list[0:j+1])
        list = list2[:]
    print(list[-1])