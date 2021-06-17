n = 0
stop = 'Y'
numlist = []
while stop != 'N':
    n = int(input('Type a number: '))
    stop = input('What to continue [Y/N]? ').upper().strip()[0]
    numlist.append(n)
print(f'The Average of the {len(numlist)} numbers typed is {sum(numlist)/len(numlist)}')
print(f'The better is {max(numlist)} the lower is {min(numlist)}')
