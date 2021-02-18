from style import blue, red, purple, none

m = float(input(f'Type a distance in {red}meters{none}: '))

print(f'This distance in {blue}kilometers{none} is {purple}{m / 1000}{none}km \n'
      f'In {blue}hectometers{none} {purple}{m / 100}{none}hm \n'
      f'In {blue}decameters{none} {purple}{m / 10}{none}dam \n'
      f'In {blue}meters{none} {purple}{m}{none} \n'
      f'In {blue}decimeters{none} {purple}{m * 10}{none}dm \n'
      f'In {blue}centimeters{none} {purple}{m * 100}{none}cm \n'
      f'And in {blue}millimeters{none} {purple}{m * 1000}{none}mm')
