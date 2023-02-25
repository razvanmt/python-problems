def autori():
    s = input()

    s1 = s.split("-")
    initials = []

    for i in s1:
        initials.append(i[0][:1])

    final = ''.join(initials)
    print(final)


autori()
