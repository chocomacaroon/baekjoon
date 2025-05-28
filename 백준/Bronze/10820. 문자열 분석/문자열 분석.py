while True:
  try:
    low = 0
    up = 0
    digit = 0
    space = 0
    s = input()
    for c in s:
      if c.islower():
        low+=1
      elif c.isupper():
        up+=1
      elif c.isdigit():
        digit+=1
      elif c == " ":
        space+=1
    print(f"{low} {up} {digit} {space}")
  except EOFError:
    break