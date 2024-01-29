height = []
for i in range(9):
    height.append(int(input()))
height.sort()
sum = sum(height)
for i in range(0,8):
     for j in range(i+1,9):
         if sum-height[i]-height[j] == 100:
             height.remove(height[i])
             height.remove(height[j-1])
             break
     if len(height) < 9:
         break
print(*height,sep='\n')