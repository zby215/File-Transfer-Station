doubles = 0
counter = 0

while doubles < 100:
    score1 = int(input('Enter the first dice score: '))
    score2 = int(input('Enter the second dice score: '))

    print('')

    counter = counter + 1

    if score1 == score2:
        doubles = doubles + 1

percent = (doubles / counter) * 100

print('Percentage doubles thrown: ', percent)
