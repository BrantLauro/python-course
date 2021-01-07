name = input('What`s your \033[32mcomplete name\033[m? ').strip().upper()

firstname = name.split()[0]

if firstname == 'LAURO':
    print('What \033[1;30mbeautiful\033[m name do you have?')
else:
    print('Your name is so \033[1;30mstandard!\033[m')

print('\033[7;30mGood Morning!\033[m')
