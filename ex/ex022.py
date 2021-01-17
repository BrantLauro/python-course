nome = str(input('Type your complete name: ')).strip()

print(f'Your name to upper case is {nome.upper()} \n'
      f'Your name to lower case is {nome.lower()} \n'
      f'Your complete name had {len(nome) - nome.count(" ")} letters on total')

nome = nome.split()

print(f'Seu primeiro nome tem {len(nome[0])} letras no total')
