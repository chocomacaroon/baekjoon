vertices = []
for i in range(9):
   vertices.append(list(map(int, input().split())))
max_value = 0
for vertice in vertices:
    max_value = max(max(vertice), max_value)
    if max_value == max(vertice):
      max_index = vertice.index(max_value)
      max_index2 = vertices.index(vertice)
print(max_value)
print(max_index2+1, max_index+1)