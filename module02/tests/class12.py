name = input('What is your name? ').upper().strip()

if name in ('LAURO, ALANNA, CECILIA, JOHN, SILVIA'):
    print('What a beautiful name you have?')
elif name in ('PEDRO, JOÃO, MATEUS, LUCAS, ZÉ'):
    print('Your name is very popular in Brazil. Cool!')
elif name in ('ANNA, MARIA, JULIA, AMANDA, JOANA'):
    print('Nice female name!')
else:
    print(f'Nice name {name}!')
print('Have a nice day!')
