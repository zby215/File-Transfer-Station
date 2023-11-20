number = int(input('Enter a number: '))

highest = number
lowest = number

while True:
    if number > highest:
        highest = number
    elif number < lowest:
        lowest = number

    number = int(input('Enter another number: '))

    if number == -1:
        break

print('The highest was:', highest)
print('The lowest was:', lowest)
