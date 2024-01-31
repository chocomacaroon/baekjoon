from collections import deque
N = int(input())
card = [i+1 for i in range(N)]
card = deque(card)
while True:
    if len(card) == 1:
        print(*card)
        break
    card.remove(card[0])
    card.rotate(-1)