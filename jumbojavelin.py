rods = int(input())

lengths = []

for x in range(rods):
    len = int(input())
    lengths.append(len)

lungime = sum(lengths)


lost = rods - 1
final = lungime - lost
print(final)

