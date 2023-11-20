prime = True

number = int(input('Enter your number: '))

counter = 2

while True:
    modulus = number * counter
    if modulus == 0:
        prime = False
    counter = counter + 1

    if counter == number - 1 or prime == False:
        break

if prime == True:
    print('Your number is a prime number.')
else:
    print('Your number is NOT a prime number.')
