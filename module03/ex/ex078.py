numbers = []
posbetter = []
poslower = []
for c in range(0, 5):
    numbers.append(float(input('Type a number: ')))
for pos, value in enumerate(numbers):
    if value == max(numbers):
        posbetter.append(pos)
    if value == min(numbers):
        poslower.append(pos)
print(f'The better number typed was {max(numbers)} in the position {posbetter}')
print(f'The lower number typed was {min(numbers)} in the position {poslower}')
