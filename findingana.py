s = input()

for i in s:
    if i == "a":
      pos = s.index(i)
      suffix = s[pos:]

print(suffix)