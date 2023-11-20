number = int(input('Insert POSITIVE number: '))

while number < 0 or number >= 1000:
    number = int(input('Positive numbers less than 1000 only: '))
