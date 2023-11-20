number = int(input('Enter a number: '))

highest = number
lowest = number

while number != -1:
    if number > highest:
        highest = number
    elif number < lowest:
        lowest = number

    number = int(input('Enter another numberL: '))

print('The highest was:', highest)
print('The lowest was:', lowest)
