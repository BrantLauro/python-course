n1 = float(input('Type a \033[1;30mvalue\033[m: '))
n2 = float(input('Type another \033[1;30mvalue\033[m: '))

print(f'The \033[7;30msum\033[m is {n1 + n2} \n'
      f'The \033[7;30msubtraction\033[m is {n1 - n2} \n'
      f'The \033[7;30mmultiplication\033[m is {n1 * n2} \n'
      f'The \033[7;30mdivision\033[m is {n1 / n2 :.1f} \n'
      f'The \033[7;30mpower\033[m is {n1 ** n2} \n'
      f'The \033[7;30mentire\033[m division is {n1 // n2} \n'
      f'The \033[7;30mdivision\033[m rest is {n1 % n2}')
