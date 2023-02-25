def oddecho():
    n = int(input())

    words_dict = {}

    for i in range(n):
        words = input()
        words_dict[i + 1] = words

    for x, y in words_dict.items():
        if (x % 2 != 0):
            print(y)

oddecho()