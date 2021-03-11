numbers = (int(input('Type a number: ')), int(input('Type a number: ')), int(input('Type a number: ')), int(input('Type a number: ')))
print(f'You typed {numbers}')

if 9 not in numbers:
    print('9 is not in the typed numbers!')
else:
    print(f'In the typed numbers there are {numbers.count(9)} Nines')

if 3 not in numbers:
    print('3 is not in the typed numbers!')
else:
    print(f'3 is in the position {numbers.index(3) + 1}')

pairs = 0

for c in numbers:
    if c % 2 == 0:
        pairs += 1

print(f'There are {pairs} pair numbers')
