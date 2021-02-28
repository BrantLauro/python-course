from random import randint
from time import sleep

print('-=-' * 22)
print('-=- I will think in a number between 0 and 10. Try to guess... -=-')
print('-=-' * 22)

n = int(input('What number I thought? '))
r = randint(0, 10)
tries = 1

print('PROCESSING...')

sleep(2)

while n != r:
    if n > r:
        n = int(input(f'OH NO! You missed, The number is less! Try again: '))
        tries += 1
        print('PROCESSING...')
        sleep(2)
    elif n < r:
        n = int(input(f'OH NO! You missed, The number is better! Try again: '))
        tries += 1
        print('PROCESSING...')
        sleep(2)

if n == r:
    print('CONGRATULATIONS! You won!')
    print(f'With {tries} tries')
