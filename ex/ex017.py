from math import hypot

co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adijacente? '))
h = hypot(co, ca)

print(f'a hipotenusa do triângulo cujo cateto oposto e cateto adijacente medem respectivamente {co} e {ca} é {h:.2f}')
