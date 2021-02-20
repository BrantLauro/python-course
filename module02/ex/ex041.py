swimmer_age = int(input('What is the swimmer age? '))

if swimmer_age <= 9:
    print(f'With {swimmer_age} years old you fit in the child category')
elif swimmer_age <= 14:
    print(f'With {swimmer_age} years old you fit in the infant category')
elif swimmer_age <= 19:
    print(f'With {swimmer_age} years old you fit in the junior category')
elif swimmer_age <= 20:
    print(f'With {swimmer_age} years old you fit in the senior category')
else:
    print(f'With {swimmer_age} years old you fit in the master category')
