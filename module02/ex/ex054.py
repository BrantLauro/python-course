from datetime import date

year = date.today().year
adults = 0
not_adults = 0

for c in range(0,7):
    birth = int(input('What your birth year? '))
    age = year - birth
    if age >= 18:
        adults += 1
    else:
        not_adults += 1
print(f'There is {adults} adults and {not_adults} kids')