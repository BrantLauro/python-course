from math import sqrt, ceil
from style import blue, none

n = float(input(f'Type a {blue}number{none}: '))
s = sqrt(n)

print(f'The {blue}square root{none} of {blue}{n}{none} is {blue}{ceil(s)}{none}')
