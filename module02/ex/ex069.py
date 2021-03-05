adults = men = women_20yo = 0

while True:
    print('~'*15)
    print('REGISTER PEOPLE')
    print('~'*15)
    age = int(input('How old are you? '))
    choose = ' '
    gender = ' '
    while gender not in 'MF':
        gender = input('What is your gender? [M/F] ').strip().upper()[0]
    if age >= 18:
        adults += 1
    if gender == 'M':
        men += 1
    if gender == 'F':
        if age <= 20:
            women_20yo += 1
    while choose not in 'YN': 
        choose = input('Want to continue? [Y/N] ').strip().upper()[0]
    if choose == 'N':
        print('Stop')
        break
print(f'At all have been registered {adults} adults. {men} men. {women_20yo} Women under or with 20')
