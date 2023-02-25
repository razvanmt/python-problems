def chanukah():
    sets = int(input())
    solution = {}
    
    for k in range(sets):
        inp = input().split(" ")
        increment = int(inp[0])
        days = int(inp[1])
        total = (days * (days + 1) // 2) + days
        solution[increment] = total

    for key, value in solution.items():
        print(key, value)


chanukah()

