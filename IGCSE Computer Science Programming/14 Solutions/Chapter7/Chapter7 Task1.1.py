number = int(input('Input number to multiply: '))
number_required = int(input('Input required number of multiples: '))

for counter in range(1, number_required + 1):
    multiple = number * counter
    print(multiple)
