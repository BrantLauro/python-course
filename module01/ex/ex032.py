from datetime import date

y = int(input('What Year? Put 0 to analyze the current year: '))
if y == 0:
    y = date.today().year

if y % 100 != 0 and y % 4 == 0 or y % 400 == 0:
    print(f'The year {y} is leap')
else:
    print(f'The year {y} is not leap')
