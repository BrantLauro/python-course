from exercicios.stile import bold, whiteblack, none
n = int(input(f'Type a int {bold}number{none} to see its {whiteblack}multiplication table{none}: '))

print('-' * 12)

print(f'{bold}{n}{none} x 01 = {whiteblack}{n * 1}{none} \n'
      f'{bold}{n}{none} x 02 = {whiteblack}{n * 2}{none} \n'
      f'{bold}{n}{none} x 03 = {whiteblack}{n * 3}{none} \n'
      f'{bold}{n}{none} x 04 = {whiteblack}{n * 4}{none} \n'
      f'{bold}{n}{none} x 05 = {whiteblack}{n * 5}{none}\n'
      f'{bold}{n}{none} x 06 = {whiteblack}{n * 6}{none} \n'
      f'{bold}{n}{none} x 07 = {whiteblack}{n * 7}{none} \n'
      f'{bold}{n}{none} x 08 = {whiteblack}{n * 8}{none} \n'
      f'{bold}{n}{none} x 09 = {whiteblack}{n * 9}{none} \n'
      f'{bold}{n}{none} x 10 = {whiteblack}{n * 10}{none}')

print('-' * 12)
