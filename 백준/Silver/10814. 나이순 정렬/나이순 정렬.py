N = int(input())
member = []
for i in range(N):
    age , name = input().split()
    member.append([int(age), name])
member.sort(key=lambda member:member[0])
for i in member:
  print(i[0], i[1])