from style import blue, green, purple, red, none
from random import choice
from time import sleep

print(f"{'='*20} {green}JOKENPO{none} {'='*20}")
print(f'''Let's play JOKENPO. {blue}Choose your play:{none}
[1] {purple}Rock{none} 
[2] {purple}Paper{none}
[3] {purple}Scissor{none}''')
play = int(input('Your Choose: '))
pc = [1, 2, 3]
pc_choice = choice(pc)

print(f'{green}JO')
sleep(1)
print('KEN')
sleep(1)
print(f'PO!!!{none}')

print(f"{'=-'*13}=-=")
if play == 1:
    if pc_choice == 3:
        print(f'Pc chose {green}scissor{none}! You {purple}WON{none}!')
    elif pc_choice == 2:
        print(f'Pc chose {green}paper{none}! You {red}LOST{none}!')
    elif pc_choice == 1:
        print(f'Pc chose {green}rock{none}! {blue}TIED{none}!')
elif play == 2:
    if pc_choice == 1:
        print(f'Pc chose {green}rock{none}! You {purple}WON{none}!')
    elif pc_choice == 3:
        print(f'Pc chose {green}scissor{none}! You {red}LOST{none}!')
    elif pc_choice == 2:
        print(f'Pc chose {green}paper{none}! {blue}TIED{none}!')
elif play == 3:
    if pc_choice == 2:
        print(f'Pc chose {green}paper{none}! You {purple}WON{none}!')
    elif pc_choice == 1:
        print(f'Pc chose {green}rock{none}! You {red}LOST{none}!')
    elif pc_choice == 3:
        print(f'Pc chose {green}scissor{none}! {blue}TIED{none}!')
else:
    print('[ERROR] Verify tha data and try again!')
print(f"{'=-'*13}=-=")
