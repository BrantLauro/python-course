d = float(input('Qual a distância em kms da viagem? '))

if d <= 200:
    print(f'A passagem ficará R${d * 0.50:.2f}')
else:
    print(f'A passagem ficará R${d * 0.45:.2f}')
