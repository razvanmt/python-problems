def betting():
    percentage = input()
    payout_ratio_1 = 100 / int(percentage)
    payout_ratio_2 = 100 / (100 - int(percentage))

    print(payout_ratio_1)
    print(payout_ratio_2)


betting()
