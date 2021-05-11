import datetime

worker = {}

print('=' * 30)
print(f'{"WORKER REGISTRATION":>24}')
print('=' * 30)

worker['name'] = input('Name: ').strip()
year_born = int(input('Year of born: '))
worker['age'] = (datetime.date.today().year) - (year_born)
worker['work_card'] = int(input('Work Card (Type 0 if you have not): '))

if worker['work_card'] != 0:
    worker['year_contracting'] = int(input('Year of contracting: '))
    worker['salary'] = int(input('Salary: $ '))
    worker['retirement_age'] = 35 + (worker['year_contracting'] - year_born)

print('=' * 30)
print(f"The name is {worker['name']}")
print(f"The age is {worker['age']}")

if worker['work_card'] == 0:
    print('There is no ctps')
else:
    print(f"The ctps is {worker['work_card']}")
    print(f"The salary is ${worker['salary']}")
    print(f"The age of retirement is {worker['retirement_age']}")
