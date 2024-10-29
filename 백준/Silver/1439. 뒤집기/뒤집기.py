S = input()

ones_list = []
zeros_list = []

tmp = ""
ones = ""
zeros = ""
tmp = ""

for c in S:
    if c == "1":
        if len(ones) and tmp[-1] == "0":
            ones_list.append(ones)
            ones = ""
        ones += c
    elif c == "0":
        if len(zeros) and tmp[-1] == "1":
            zeros_list.append(zeros)
            zeros = ""
        zeros += c
    tmp += c
if len(zeros):
    zeros_list.append(zeros)
if len(ones):
    ones_list.append(ones)

print(min(len(ones_list),len(zeros_list)))