N = input()
M = input()
N = int(N[:-2]+"00")

for i in range(100):
    if int(str(N+i))%int(M)==0:
        print(str(N+i)[-2:])
        break
if i == 100:
    print("00")