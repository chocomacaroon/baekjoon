n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10  # a의 1의 자리만 사용
    if a == 0:
        print(10)  # 1의 자리가 0이면 결과는 항상 10
        continue

    # 1의 자리가 반복되는 패턴 찾기
    pattern = []
    c = a
    while c not in pattern:
        pattern.append(c)
        c = (c * a) % 10

    # b가 패턴 길이의 배수일 때는 마지막 값을 사용
    index = b % len(pattern)
    if index == 0:
        print(pattern[-1])
    else:
        print(pattern[index - 1])
