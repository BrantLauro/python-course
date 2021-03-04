n = 0
numlist = []
while n != 999:
    n = int(input('Type a number (type 999 to stop): '))
    numlist.append(n)
print(f'The sum of the {len(numlist) - 1} numbers typed is {sum(numlist) - 999}')
