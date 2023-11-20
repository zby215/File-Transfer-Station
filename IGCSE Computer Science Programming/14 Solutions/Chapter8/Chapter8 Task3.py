total = 0
sixes = 0

for i in range(100):
    score = int(input('Enter the dice score: '))
    total = total + score

    if score == 6:
        sixes = sixes + 1

average = total / 100

print('Sixes', sixes)
print('Average', average)
