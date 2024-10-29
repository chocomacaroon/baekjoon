N = int(input())
paper = []
width_max = 0
height_max = 0
for _ in range(N):
    a,b = map(int, input().split())
    paper.append([a,b])
    width_max = max(width_max, a+10)
    height_max = max(height_max, b+10)
paper_result = []
for _ in range(height_max):
    paper_result.append([0]*(int(width_max)))

for a,b in paper:
    for i in range(a,a+10):
        for j in range(b,b+10):
            paper_result[j][i] = 1

sum = 0
for m in paper_result:
    sum += m.count(1)
print(sum)