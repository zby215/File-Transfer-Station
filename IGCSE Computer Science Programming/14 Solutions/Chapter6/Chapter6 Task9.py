large_petrol = 0.296
small_petrol = 0.208
large_diesel = 0.236
small_diesel = 0.176

fuel = input('Input "P" for petrol and "D" for diesel: ')
size = input('Input "L" larger than 2 litres and "S" for less: ')
distance = int(input('Input annual mileage: '))

if fuel == 'P' and size == 'L':
    emission = large_petrol * distance / 1000
elif fuel == 'P' and size == 'S':
    emission = small_petrol * distance / 1000
elif fuel == 'D' and size == 'L':
    emission = large_diesel * distance / 1000
elif fuel == 'D' and size == 'S':
    emission = small_diesel * distance / 1000
else:
    emission = 'Error!'

print(emission)
