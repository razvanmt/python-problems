s = input()

for i in s:
  c = s.count("e")
  double = "e" * c

  response = s[:1] + double + s[1:]

  
print(response)


