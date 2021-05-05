numbers = [[], []]
number = 0

for c in range(0, 7):
    number = int(input('Type a number: '))
    print(30*'-')
    if number % 2 == 0:
        numbers[0].append(number)
    else:
        numbers[1].append(number)


numbers[0].sort()
numbers[1].sort()
print(f'The pair numbers are {numbers[0]}')
print(f'The odd numbers are {numbers[1]}')
