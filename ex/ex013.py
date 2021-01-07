s = float(input('Qual o salário? R$'))
a = float(input('Qual a porcentagem de aumento? '))
ns = s + s * (a / 100)

print(f'O salário {s:.2f} com a promoção de {a}% ficou {ns :.2f}')
