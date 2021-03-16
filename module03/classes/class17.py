numbers = []
for c in range(0, 5):
    numbers.append(int(input('Type a number: ')))
for pos, c in enumerate(numbers):
    print(f'Number {c} in position {pos}')
