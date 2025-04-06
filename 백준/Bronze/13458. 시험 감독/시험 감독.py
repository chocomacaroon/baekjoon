N = int(input())
students = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0
if B >= C:
    for s in students:
        answer += 1
        # print(1, end=' ')
        if s > B:
            s -= B
            answer += (int(bool(s % C)) + s//C)
            # print((int(bool(s % C)) + s//C))
        else:
            pass
            # print(0)
    print(answer)
else:
    for s in students:
        answer += 1
        s -= B
        answer += int(bool(s % C))+s//C
    print(answer)

