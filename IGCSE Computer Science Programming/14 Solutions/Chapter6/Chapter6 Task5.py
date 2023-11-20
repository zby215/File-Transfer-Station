student_mark = int(input('Input STUDENTE mark: '))
max_mark = int(input('Input MAXIMUM mark: '))

percentage = (student_mark / max_mark) * 100

if student_mark >= 80:
    print('Grade A')
elif student_mark >= 70:
    print('Grade B')
elif student_mark >= 60:
    print('Grade C')
else:
    print('Grade U')
