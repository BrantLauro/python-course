from style import bold, blue, none
n = int(input(f'Type a int {bold}number{none} to see its {blue}multiplication table{none}: '))

print('-' * 12)

print(f'{bold}{n}{none} x 01 = {blue}{n * 1}{none} \n'
      f'{bold}{n}{none} x 02 = {blue}{n * 2}{none} \n'
      f'{bold}{n}{none} x 03 = {blue}{n * 3}{none} \n'
      f'{bold}{n}{none} x 04 = {blue}{n * 4}{none} \n'
      f'{bold}{n}{none} x 05 = {blue}{n * 5}{none}\n'
      f'{bold}{n}{none} x 06 = {blue}{n * 6}{none} \n'
      f'{bold}{n}{none} x 07 = {blue}{n * 7}{none} \n'
      f'{bold}{n}{none} x 08 = {blue}{n * 8}{none} \n'
      f'{bold}{n}{none} x 09 = {blue}{n * 9}{none} \n'
      f'{bold}{n}{none} x 10 = {blue}{n * 10}{none}')

print('-' * 12)
