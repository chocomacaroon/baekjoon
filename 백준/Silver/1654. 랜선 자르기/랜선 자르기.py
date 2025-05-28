K,N = map(int, input().split())

lan = [int(input()) for _ in range(K)]
start = 1
end = max(lan)

answer = 0

while start <= end:
    mid = (start+end)//2
    total = 0

    for n in lan:
        total += (n//mid)
    if total >= N:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)