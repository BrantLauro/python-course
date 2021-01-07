p = float(input('Qual o preço do produto? R$'))
des = float(input('Qual é o desconto? '))
d = p - p * (des/100)

print(f'O novo preço com o desconto de {des}% é {d:.2f}')
