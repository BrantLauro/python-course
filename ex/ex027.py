nome = str(input('Qual é o seu nome? ')).strip().split()

print(f'Muito Prazer em te conhecer! \n'
      f'Seu primeiro nome é {nome[0]} \n'
      f'Seu último nome é {nome[len(nome) - 1]}')
