import sys

input = sys.stdin.readline

N = int(input().strip())
record = []
rank = [1]*N

for i in range(N):
    x,y = map(int,input().strip().split())
    record.append([x,y])

for x,y in record:
    for j in range(len(record)):
        a,b = record[j]
        if a < x and b < y:
            rank[j]+=1
print(*rank)