students = [[]]
c = 0
def lin():
    print('='*30)

while True:
    students[c].append(input('Name: ').strip())
    students[c].append(float((input('1° Grade: '))))
    students[c].append(float((input('2° Grade: '))))
    c += 1
    choice = ' '
    while choice not in 'NY':
        choice = input('Do you want to continue? [Y/N] ').upper().strip()[0]
    if choice == 'N':
        break
    if choice == 'Y':
        students.append([])
        lin()
print(students)
lin()
print(f'{"No.":<4}{"NAME":<10}{"GRADE":>8}')
lin()
for d in range(0, len(students)):
    print(f'{d:<4} {students[d][0]:<10} {(students[d][1] + students[d][2])/2:>8.1f} \n')
while True:
    student = int((input('Do you want to see which students grades? [999 to stop] ')))
    if student == 999:
        break
    if student <= len(students) - 1:
        lin()
        print(f'The notes of {students[student][0]} are {students[student][1]} and {students[student][2]}')
