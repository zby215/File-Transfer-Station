names = [None] * 30
squad_shots = [None] * 30
squad_assists = [None] * 30
squad_goals = [None] * 30
success_index = [None] * 30

for i in range(3):
    name = input("Enter player's name: ")
    names[i] = name

    while True:
        shots = int(input("Enter shots made: "))
        if shots > 100 or shots < 0:
            print("Error: Unexpected input")
        else:
            break

    while True:
        assists = int(input("Enter assists made: "))
        if assists > 50 or assists < 0:
            print("Error: Unexpected input")
        else:
            break

    while True:
        goals = int(input("Enter goals scored: "))
        if goals > 40 or goals < 0:
            print("Error: Unexpected input")
        else:
            break

squad_shots[i] = shots
squad_assists[i] = assists
squad_goals[i] = goals

print(names)
print(squad_goals)
print(squad_assists)
print(squad_goals)
