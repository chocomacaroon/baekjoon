N = int(input())
card = set(map(int, input().split()))
card_2 = set()
M = int(input())
card_2 = list(map(int, input().split()))
result = []
for i in card_2:
  result.append(1 if i in card else 0)
print(*result)