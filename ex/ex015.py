dias = int(input('Por quantos dias o carro ficou alugado: '))
km = float(input('Qual a quantidade de Kms rodados: '))
p = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${p :.2f}')
