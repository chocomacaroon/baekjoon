i = 0
while True:
    i+=1
    L,P,V = map(int, input().split())
    if L==P==V==0:
        break
    days = V//P*L
    if V%P < L:
        days += V%P
    else:
        days += L
    print("Case "+str(i)+": "+str(days))
