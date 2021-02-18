name = str(input('Type your complete name: ')).strip()

print(f'Your name to upper case is {name.upper()} \n'
      f'Your name to lower case is {name.lower()} \n'
      f'Your complete name had {len(name) - name.count(" ")} letters on total')

name = name.split()

print(f'Your first name had {len(name[0])} letters on total')
