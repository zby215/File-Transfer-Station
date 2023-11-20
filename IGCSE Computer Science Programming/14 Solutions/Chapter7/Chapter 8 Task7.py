minutes = 0
highest_temp = 0

start_temp = int(input('Enter the start temperature and press ENTER '))

while True:
    reaction_temp = int(input())

    minutes = minutes + 1

    if reaction_temp > highest_temp:
        highest_temp = reaction_temp
        highest_mins = minutes

        if reaction_temp <= start_temp:
            break

print('\nHighest temp:', highest_temp, 'reached at', highest_mins, 'mins')
print('Total reaction time:', minutes)
