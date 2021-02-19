from datetime import date

birth = int(input('What is your year of birth: '))
year =  date.today().year
age = year - birth

if age < 18:
    print(f'You will enlist in {18-age} years')
elif age == 18:
    print('Is time to enlist')
else:
    print(f'Enlistment time has passed {age-18} years ago')