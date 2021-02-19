n1 = int(input('Type a number: '))
n2 = int(input('Type another: '))

if n1 > n2:
    print(f'{n1} is better!')
elif n1 < n2:
    print(f'{n2} is better!')
else:
    print('They are the same!')
