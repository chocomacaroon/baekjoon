N = int(input())
S = input()
sum = 0
for i in range(N):
  sum += ord(S[i]) - ord('0')
print(sum)