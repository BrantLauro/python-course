name = str(input('What is your name? ')).strip().split()

print(f'Nice to meet you! \n'
      f'Your first name is {name[0]} \n'
      f'Your last name is {name[len(name) - 1]}')
