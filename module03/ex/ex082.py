numbers = []
pair = []
odd = []
choice = ' '
while True:
    while choice not in 'NY':
        choice = input('Do you want to add a number on the list? [Y/N] ').upper().strip()[0]
    if choice == 'N':
        break
    if choice == 'Y':
        number = int(input('Type a number: '))
        numbers.append(number)
        if number % 2 == 0:
            pair.append(number)
        else:
            odd.append(number)
        choice = ' '
print(f'The list is {numbers}')
print(f'The pair numbers are {pair}')
print(f'The odd numbers are {odd}')
