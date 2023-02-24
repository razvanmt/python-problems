w = int(input())
n = int(input())

pieces = []
areas = []

for i in range(n):
    piece = input().split(" ")
    wi = piece[0]
    li = piece[1]
    pieces.append(piece)

for i in pieces:
    a = int(i[0]) * int(i[1])
    areas.append(a)

area = sum(areas)

length = area / w

print(int(length))
