def qaly():
    periods = int(input())

    qaly = {}

    for p in range(periods):
        qy = input().split(" ")
        q = float(qy[0])
        y = float(qy[1])

        qaly[p + 1] = q * y

    print(sum(qaly.values()))


qaly()
