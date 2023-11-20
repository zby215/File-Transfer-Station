import sys


def validate(num, pwd):
    if len(pwd) < 5:
        return False
    elif num < 1000 or num > 1500:
        return False
    else:
        return True


number = int(input('Insert your number: '))
password = input('Insert your password: ')

attempts = 1
while validate(number, password) is False and attempts <= 2:
    if attempts == 2:
        print('Locked out')
        sys.exit()
    else:
        print('Error')
        number = int(input('Insert user number between 1000 and 1500: '))
        password = input('Insert a password with at least 5 characters: ')

    attempts = attempts + 1

if validate(number, password) == True:
    print('Welcome')
