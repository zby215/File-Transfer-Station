subtractions = 0

a = int(input('Enter a: '))
b = int(input('Enter b: '))

while a >= b:
    a = a - b
    subtractions = subtractions + 1

print('a Quotient b =', subtractions)
print('a Modulus b =', a)
