n1 = float(input('First number: '))
n2 = float(input('Second number: '))
n3 = float(input('Third number '))

if n1 > n2 and n1 > n3:
    print(f'The biggest is {n1}')
elif n2 > n1 and n2 > n3:
    print(f'The biggest is {n2}')
elif n3 > n1 and n3 > n2:
    print(f'The biggest is {n3}')

if n1 < n2 and n1 < n3:
    print(f'The smaller is {n1}')
elif n2 < n1 and n2 < n3:
    print(f'The smaller is {n2}')
elif n3 < n1 and n3 < n2:
    print(f'The smaller is {n3}')
