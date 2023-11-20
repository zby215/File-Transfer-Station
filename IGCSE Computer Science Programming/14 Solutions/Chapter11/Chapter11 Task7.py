def array_input(num):
    for i in range(0, 12):
        multiples[i] = num * (i + 1)


def array_display():
    for i in range(0, 12):
        print(multiples[i])


multiples = [None] * 12

action = input('''Choose from:

1.Input
2.Display
3.Exit

[1,2 or 3]?''')

while action == '1' or action == '2':
    if action == '1':
        multiples = int(input('Input a whle number: '))
        array_input(multiples)
    elif action == '2':
        array_display()
    else:
        break
    action = int(input('\nChoose [1,2 or 3]?'))
