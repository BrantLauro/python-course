numbers = []
while True:
    numbers.append(int(input('Type a number: ')))
    choice = ' '
    while choice not in 'NY':
        choice = input('Do you want to continue? [Y/N] ').upper().strip()[0]
    if choice == 'N':
        break
numbers.sort(reverse=True)
print(f'You typed {len(numbers)} numbers')
print(f'The list in a decenting order is {numbers}')
if 5 in numbers:
    print('5 is on the list')
else:
    print('5 is not on the list')
