c = eval(input())  # cost of seed per square metre
l = eval(input())  # number of lawns to sow

dim = []

for x in range(l):
    dimension = input().split(" ")
    w = float(dimension[0])
    le = float(dimension[1])
    calcul = w * le
    dim.append(calcul)

total_dimension = sum(dim)

total_cost = total_dimension * c
print('%.8f' % total_cost)