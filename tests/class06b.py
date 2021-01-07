n = input('Type \033[1;30msomething\033[m: ')

print(f'\033[33m{n.isnumeric()}')
