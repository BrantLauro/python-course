m = float(input('Type a distance in \033[34mmeters\033[m: '))

print(f'This distance in \033[34mkilometers\033[m is \033[1;30m{m / 1000}\033[mkm \n'
      f'In \033[34mhectometers\033[m \033[1;30m{m / 100}\033[mhm \n'
      f'In \033[34mdecameters\033[m \033[1;30m{m / 10}\033[mdam \n'
      f'In \033[34mmeters\033[m \033[1;30m{m}\033[mm \n'
      f'In \033[34mdecimeters\033[m \033[1;30m{m * 10}\033[mdm \n'
      f'In \033[34mcentimeters\033[m \033[1;30m{m * 100}\033[mcm \n'
      f'And in \033[34mmillimeters\033[m \033[1;30m{m * 1000}\033[mmm')
