nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome com todas as letras em maiúsculas é {nome.upper()} \n'
      f'Seu nome com todas as letras em minúsculas é {nome.lower()} \n'
      f'Seu nome completo tem {len(nome) - nome.count(" ")} letras no total')

nome = nome.split()

print(f'Seu primeiro nome tem {len(nome[0])} letras no total')
