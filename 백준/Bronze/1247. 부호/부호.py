while True:
    try:
        N = int(input())
        su = 0
        for i in range(N):
            su += int(input())
        if su == 0:
            print("0")
        elif su > 0:
            print("+")
        elif su < 0:
            print("-")
    except EOFError:
        break