student = {'name' : '', 'average' : 0 }
student['name'] = input('What is the students name? ')
student['average'] = int(input('What is the student average? '))

print('='*30)
print(f'The name is {student["name"]}')
print(f'The average is {student["average"]}')
if student['average'] >= 7:
    print('The student passed!')
else:
    print('The student did not passed!')
