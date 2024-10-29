x = int(input())

sticks = [64]
while sum(sticks)>x:
    sticks.append(sticks[0] / 2)
    sticks[0] /= 2
    if sum(sticks[1:]) >= x:
        sticks.pop(0)
    sticks.sort()
print(len(sticks))
