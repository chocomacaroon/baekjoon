vertices = []
alp = []
max_len = 0
for i in range(5):
   vertices.append(list(input()))
   max_len = max(max_len, len(vertices[i]))
for i in range(max_len):
  for j in range(5):
    if i < len(vertices[j]):
      print(vertices[j][i], end = '')