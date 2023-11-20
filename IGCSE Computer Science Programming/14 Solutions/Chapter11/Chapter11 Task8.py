ID_array = [112, 217, 126]
age = [45, 16, 27]
gender = ['M', 'F', 'F']

search_ID = int(input('Insert ID to Search: '))

for i in range(0, 3):
    if search_ID == ID_array[i]:
        print('Age:', age[i])
        print('Gender:', gender[i])
