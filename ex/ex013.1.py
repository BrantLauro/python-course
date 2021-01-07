p = float(input('Qual o preço do produto? R$'))
d = p - p * (10/100)
a = p + p * (8/100)

print(f'O preço do produto é {p} \n'
      f'A vista, ficaria {d} \n'
      f'Parcelado ficaria {a}')
