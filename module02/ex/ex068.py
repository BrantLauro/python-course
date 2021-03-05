from random import randint
n = c = 0

while True:
    choose = ''
    pc = randint(1, 10)
    n = int(input('Type a number between 1 and 10: '))
    if 1 <= n <= 10:
        choose = input('Even or Odd? [E/O] ').strip().upper()[0]
        if choose == 'E':
            if (pc + n) % 2 == 0:
                print(f'Pc choose {pc}. {pc + n} is Even! You won congrats!')
                c += 1
            else:
                print(f'Pc choose {pc}. {pc + n} is Odd! You lost, sorry!')
                break
        elif choose == 'O':
            if (pc + n) % 2 != 0:
                print(f'Pc choose {pc}. {pc + n} is Odd! You won congrats!')
                c += 1
            else:
                print(f'Pc choose {pc}. {pc + n} is Even! You lost, sorry!')
                break
        else:
            print('[ERROR] Try Again!')
    else:
        print('Type a number between 1 and 10!')
print(f'You won {c} times!')
