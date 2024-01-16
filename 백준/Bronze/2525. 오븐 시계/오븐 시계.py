h, m = map(int, input().split())
cook_time = int(input())
total_min = 60 * h + m
fin_time = total_min + cook_time
fin_h = fin_time // 60
fin_m = fin_time % 60
if fin_h >= 24:
  fin_h -= 24
print(fin_h, fin_m)