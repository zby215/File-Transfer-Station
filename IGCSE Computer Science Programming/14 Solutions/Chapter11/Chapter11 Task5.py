def search():
    letters = ['a', 'a', 'b', 'c', 'c', 'c']
    matches = 0
    user_letter = input('Enter the character to search for: ')

    for i in range(0, 6):
        if user_letter == letters[i]:
            matches = matches + 1

        return matches


number = search()

if numbers > 0:
    print('Your letter has been found', number, 'times.')
else:
    print('No match.')
