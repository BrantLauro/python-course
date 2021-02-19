grade1 = float(input('Type the first grade: '))
grade2 = float(input('Type the second grade: '))
average = (grade1 + grade2) / 2

if average < 5:
    print('DISAPPROVED')
elif average >= 5 and average < 6.9:
    print('RECOVERY')
else:
    print('OKAY')
print(average)