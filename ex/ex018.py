from math import sin, cos, tan, radians

a = float(input('Digite um ângulo: '))
ar = radians(a)

print(f'O seno do ângulo {a}° é {sin(ar) :.2f} \n'
      f'O cosseno é {cos(ar) :.2f} \n'
      f'E a tangente é {tan(ar) :.2f}')
