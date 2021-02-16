n = float(input('Type a number: '))

print(f'The double of \033[1;30m{n}\033[m is \033[1;30m{n * 2}\033[m. \n'
      f'The triple is \033[1;30m{n * 3}\033[m. \n'
      f'And the square root is \033[1;30m{pow(n , 0.5) :.2f}\033[m.')
