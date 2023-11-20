school_name = input('Enter the school name: ')
students = int(input('Enter the number of students:'))

highest = students
lowest = students
highest_name = school_name
lowest_name = school_name

for i in range(199):
    print('')

    school_name = input('Enter the school name: ')
    students = int(input('Enter the number of students: '))

    if students > highest:
        highest = students
    elif students < lowest:
        lowest = students

print('\nSchool with most students:', highest_name)
print('School with least students: ', lowest_name)
