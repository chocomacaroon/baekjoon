fir, sec, thr = map(int, input().split())
if fir == sec == thr:
    prize = 10000 + fir * 1000
elif fir != sec and sec != thr and fir != thr:
  if fir > sec: max = fir
  elif sec > fir: max = sec
  if(thr > max): max = thr
  prize = max * 100
else:
    if fir == sec or fir == thr:
        prize = 1000 + fir * 100
    else:
        prize = 1000 + sec * 100
print(prize)