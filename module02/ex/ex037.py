number = int(input('Type a number: '))
print('''chose a base for the conversion:
[1] to binary
[2] to octal
[3] to hexadecimal''')
base = int(input('Your Option: '))

if base == 1:
    print(f'{number} converted to binary is {bin(number)[2:]}')
elif base == 2:
    print(f'{number} converted to octal is {oct(number)[2:]}')
elif base == 3:
    print(f'{number} converted to hexadecimal is {hex(number)[2:]}')
else:
    print('[ERROR] Verify the input and try again')
