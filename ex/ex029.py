v = float(input('Qual é a velocidade atual do carro? '))
m = (v - 80) * 7

if v > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h \n'
          f'Você deve pagar uma multa de R${m:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
