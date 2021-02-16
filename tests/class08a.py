import math
from style import blue, none

n = float(input(f'Type a {blue}Number{none}: '))
s = math.sqrt(n)

print(f'The {blue}square root{none} of {n} is {blue}{math.ceil(s)}{none}')
