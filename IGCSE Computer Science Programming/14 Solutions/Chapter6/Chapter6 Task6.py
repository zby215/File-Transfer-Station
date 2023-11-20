local_charge = 20
international_charge = 40

international = input('Input "2" for international and "1" for local: ')
weight = float(input('Input weight of parcel: '))


def roundup(n):
    if n - int(n) > 0:
        n = int(n) + 1
    return n


if international == '2':
    if weight < 5:
        print(international_charge)
    else:
        print('Over weight')
else:
    if weight < 5:
        print(local_charge)
    else:
        excess = roundup(weight) - 5
        cost = local_charge + excess
        print(cost)
