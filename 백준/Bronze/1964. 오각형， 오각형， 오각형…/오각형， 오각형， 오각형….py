N = int(input())
dot = 5
for i in range(1, N):
    dot += 7+3*(i-1)
print(dot%45678)