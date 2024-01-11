h, m = map(int, input().split())
total = 60 * h + m
if(total >= 45):
  alarm_min = total - 45
else:
  alarm_min = total - 45 + 24 * 60
alarm_h = alarm_min // 60
alarm_m = alarm_min % 60
print(alarm_h, alarm_m)