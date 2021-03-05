from random import randint
n = c = 0
choose = ''
pc = randint(1, 10)
while True:
    n = int(input('Type a number between 1 and 10: '))
    if 1 <= n <= 10:
        choose = input('Even or Odd? [E/O] ').strip().upper()[0]
        if choose == 'E':
            if (pc + n) % 2 == 0:
                print(f'Pc choose {pc}. {pc + n} is Even! You won congrats!')
                pc = randint(1, 10)
            else:
                print(f'Pc choose {pc}. {pc + n} is Odd! You lose, sorry!')
                break
        elif choose == 'O':
            if (pc + n) % 2 != 0:
                print(f'Pc choose {pc}. {pc + n} is Odd! You won congrats!')
                pc = randint(1, 10)
            else:
                print(f'Pc choose {pc}. {pc + n} is Even! You lose, sorry!')
                break
        else:
            print('[ERROR] Try Again')
    else:
        print('Type a number between 1 and 10')
