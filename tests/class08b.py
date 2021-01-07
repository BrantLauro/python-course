from math import sqrt, ceil

n = float(input('Type a \033[1;30mnumber\033[m: '))
s = sqrt(n)

print(f'The \033[35msquare root\033[m of \033[1;30m{n}\033[m is \033[1;30m{ceil(s)}\033[m')
