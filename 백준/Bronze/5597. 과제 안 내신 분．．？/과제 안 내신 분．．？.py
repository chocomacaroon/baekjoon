students = [i+1 for i in range(0, 30)]
while True:
  try:
    n = int(input())
    students.remove(n)
  except:
    break;
print(min(students))
print(max(students))