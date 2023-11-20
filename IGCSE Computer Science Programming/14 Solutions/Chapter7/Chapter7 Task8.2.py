total = 0
while True:
    number = int(input('Enter number: '))
    total = total + number

    if number == -1:
        break

total = total + 1

print(total)
