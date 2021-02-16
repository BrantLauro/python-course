from style import blue, none

name = input(f'What`s your {blue}complete name{none}? ').strip().upper()

firstname = name.split()[0]

if firstname == 'LAURO':
    print(f'What {blue}beautiful{none} name do you have?')
else:
    print(f'Your name is so {blue}standard!{none}')

print(f'{blue}Good Morning!{none}')
