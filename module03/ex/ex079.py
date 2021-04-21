numbers = []
while True:
    number = (int(input('Type a number: ')))
    if number not in numbers:
        numbers.append(number)
    else:
        print('This number is already on the list')
    choice = (input('Want to continue: [Y/N] ')).upper().strip()[0]
    if choice == 'N':
        break
numbers.sort()
print(numbers)
