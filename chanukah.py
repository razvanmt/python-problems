def chanukah():
    sets = int(input())
    dict = {}
    for k in range(sets):
        days = int(input())
        total = (days * (days + 1) // 2) + days
        dict[k + 1] = total

    for key, value in dict.items():
        print(key, value)


chanukah()
