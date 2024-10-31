N,B = map(int, input().split())
answer = ""
while True:
    if N % B >= 10:
        answer += chr(N%B+55)
    else:
        answer += str(N % B)
    N //= B
    if N == 0:
        break
print(answer[::-1])