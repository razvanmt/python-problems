input = input().split(" ")

x = int(input[0])
y = int(input[1])
n = int(input[2])

for i in range(1, n + 1):
    if (i % x == 0 and i % y == 0):
        i = "FizzBuzz"
    elif (i % x == 0):
        i = "Fizz"
    elif (i % y == 0):
        i = "Buzz"
    print(i)
