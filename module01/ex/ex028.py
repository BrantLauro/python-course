from random import randint
from time import sleep

print('-=-' * 22)
print('-=- I will think in a number between 0 and 5. Try to guess... -=-')
print('-=-' * 22)

n = int(input('What number I thought? '))
r = randint(0, 5)

print('PROCESSING...')

sleep(2)

if n == r:
    print('CONGRATULATIONS! You won!')
else:
    print(f'OH NO! You missed! I thought in number {r} not {n}')
