from style import blue, none

n1 = float(input(f'Type a {blue}value{none}: '))
n2 = float(input(f'Type another {blue}value{none}: '))

print(f'The {blue}sum{none} is {n1 + n2} \n'
      f'The {blue}subtraction{none} is {n1 - n2} \n'
      f'The {blue}multiplication{none} is {n1 * n2} \n'
      f'The {blue}division{none} is {n1 / n2 :.1f} \n'
      f'The {blue}power{none} is {n1 ** n2} \n'
      f'The {blue}entire{none} division is {n1 // n2} \n'
      f'The {blue}division{none} rest is {n1 % n2}')
