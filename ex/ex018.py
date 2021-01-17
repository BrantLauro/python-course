from math import sin, cos, tan, radians

a = float(input('Type a angle: '))
ar = radians(a)

print(f'The sine of the angle {a}° is {sin(ar) :.2f} \n'
      f'The cosine is {cos(ar) :.2f} \n'
      f'And the tangent is {tan(ar) :.2f}')
