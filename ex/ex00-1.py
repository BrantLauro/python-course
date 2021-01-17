from ex.style import none, bold, red
from datetime import date

year = int(input(f'What {bold}year{none} were you born? '))
month = (input(f'What {bold}month{none} were you born? '))
day = int(input(f'What {bold}day{none} were you born? '))

print(f'You were born on {red}{month}{none} {red}{day}{none}, {red}{year}{none}. Correct?')
print(f'You are {red}{date.today().year-year}{none} years old!')
