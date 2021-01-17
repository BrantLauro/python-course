from ex.style import none, whiteblack

a = input('Type something: ')

print(f'This value type is: {whiteblack}{type(a)}{none} \n'
      f'Just has space? {whiteblack}{a.isspace()}{none} \n'
      f'Is a number? {whiteblack}{a.isnumeric()}{none} \n'
      f'Is alpha? {whiteblack}{a.isalpha()}{none} \n'
      f'Is alphanumeric? {whiteblack}{a.isalnum()}{none} \n'
      f'Is upper? {whiteblack}{a.isupper()}{none} \n'
      f'Is lower? {whiteblack}{a.islower()}{none} \n'
      f'Is a title? {whiteblack}{a.istitle()}{none}')
