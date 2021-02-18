from style import blue, none

a = input('Type something: ')

print(f'This value type is: {blue}{type(a)}{none} \n'
      f'Just has space? {blue}{a.isspace()}{none} \n'
      f'Is a number? {blue}{a.isnumeric()}{none} \n'
      f'Is alpha? {blue}{a.isalpha()}{none} \n'
      f'Is alphanumeric? {blue}{a.isalnum()}{none} \n'
      f'Is upper? {blue}{a.isupper()}{none} \n'
      f'Is lower? {blue}{a.islower()}{none} \n'
      f'Is a title? {blue}{a.istitle()}{none}')
