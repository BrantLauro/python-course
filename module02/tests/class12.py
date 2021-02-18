name = input('What is your name? ')

if name in ('Lauro, Alanna, Cecilia, John, Silvia'):
    print('What a beautiful name you have?')
elif name in ('Pedro, João, Mateus, Lucas, Zé'):
    print('Your name is very popular in Brazil. Cool!')
elif name in ('Anna, Maria, Julia, Amanda, Joana'):
    print('Nice female name!')
else:
    print(f'Nice name {name}!')
print('Have a nice day!')