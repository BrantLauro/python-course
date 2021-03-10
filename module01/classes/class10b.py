from style import blue, none

n1 = float(input(f'Type a {blue}fist grade{none}: '))
n2 = float(input(f'Type a {blue}second grade{none}: '))

a = (n1+n2)/2

print(f'Your average was {blue}{a:.1f}{none}')

if a >= 6.0:
    print(f'{blue}Congratulations!{none} Your grades are great!')
else:
    print(f'{blue}Study more!{none} Your grades are not so good!')

print(f'{blue}Have a good day!')
