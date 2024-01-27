register = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
val = str(register.index(input()))
val = val + str(register.index(input()))
for _ in range(register.index(input())):
    val += '0'
print(int(val))