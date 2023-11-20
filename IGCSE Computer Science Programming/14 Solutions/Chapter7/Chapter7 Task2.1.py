answer = 1
a = int(input('Enter a: '))
b = int(input('Enter b: '))

for counter in range(b):
    answer = answer * a

print(answer)
print(a ** b)
