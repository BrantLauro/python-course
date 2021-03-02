menu = 0
n1 = float(input('Type a number: '))
n2 = float(input('Type another: '))
while menu != 5:
    menu = int(input('''
    [1] Sum
    [2] Multiply
    [3] Better
    [4] New Númbers
    [5] Quit
    
    Your choice: '''))

    if menu == 1:
        print(f'The Sum is {n1+n2}')
    elif menu == 2:
        print(f'The Multiplication is {n1*n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'The better is {n1}')
        elif n2 > n1:
            print(f'The better is {n2}')
        else:
            print(f'They are equal')
    elif menu == 4:
        print('Choose again: ')
        n1 = float(input('Type a number: '))
        n2 = float(input('Type another: '))
    else:
        print('[ERROR]. Verify the data and try again!')
