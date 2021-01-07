import math

n = float(input('Type a \033[35;41mNumber\033[m: '))
s = math.sqrt(n)

print(f'The \033[7;30msquare root\033[m of {n} is \033[43m{math.ceil(s)}\033[m')
