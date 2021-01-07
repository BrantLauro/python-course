from random import randint
from time import sleep

print('-=-' * 19)
print('-=- Vou pensar em número de 0 a 5! Tente adivinhar... -=-')
print('-=-' * 19)

n = int(input('Em que número eu pensei? '))
s = randint(0, 5)

print('PROCESSANDO...')

sleep(2)

if n == s:
    print('PARABÉNS! Você acertou!')
else:
    print(f'OH NÃO! Você errou! Eu penei no número {s} não no {n}')
