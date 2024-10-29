num = []
Fiz = []
i = 0
for _ in range(3):
    n = input()
    if n.isdigit():
        break
    i+=1

i = int(n) + (3-i)

if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 3 == 0 and i % 5 != 0:
    print("Fizz")
elif i % 3 != 0 and i % 5 == 0:
    print("Buzz")
elif i % 3 != 0 and i % 5 != 0:
    print(str(i))