from style import green, red

number = int(input('Type a number: '))
total = 0

for c in range(1, number+1):
    if number % c == 0:
        print(f'{green}', end=' ')
        total += 1
    else:
        print(f'{red}', end=' ')
    print(f'{c}', end=' ')

if total == 2:
    print(f'{green}Prime')
else:
    print(f'{red}Not Prime')
