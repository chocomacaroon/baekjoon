day = [31,28,31,30,31,30,31,31,30,31,30,31]
yoil = ["SUN", "MON", "TUE", "WED","THU", "FRI", "SAT"]
x,y = map(int,input().split())
days = y
for n in range(x-1):
    days += day[n]
print(yoil[days%7])