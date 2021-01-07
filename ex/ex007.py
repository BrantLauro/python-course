g1 = float(input('The student`s \033[3;30m1st grade\033[m: '))
g2 = float(input('The student`s \033[3;30m2nd grade\033[m: '))
a = (g1 + g2) / 2

print(f'The average between \033[3;30m{g1}\033[m and \033[3;30m{g2}\033[m is \033[3;30m{a :.1f}\033[m')
