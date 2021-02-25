ages = []
man_ages = []
older_man = ''
women_under_20 = 0

for c in range (1, 5):
    print(f"{'-'*12} {c}° Person {'-'*12}")
    name = input('What is your name? ').strip()
    age = int(input('How old are your? '))
    gender = input('What is your gender [M/F]? ').upper().strip()
    ages.append(age)
    if gender == 'M':
        man_ages.append(age)
        if max(man_ages) == age:
            older_man = name
    elif gender == 'F' and age <= 20:
        women_under_20 += 1
    else:
        print('[ERROR] Verify the data and try again!')

average = sum(ages) / len(ages)
print(f'The average age is {average}')
print(f'The older man is {older_man} with {max(man_ages)} years old')
print(f'There is {women_under_20} women under 20 years old')
