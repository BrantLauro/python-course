from math import hypot

oside = float(input('What is the length of the opposite side? '))
aside = float(input('What is the length of the adjacent side? '))
h = hypot(oside, aside)

print(f'The hypotenuse of the triangle whose opposite side and adjacent side measure respectively {oside} and {aside} is {h:.2f}')
