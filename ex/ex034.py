s = float(input('Qual é o salário do funcionário? R$'))

if s > 1250.00:
    dez = s + s * 0.10
    print(f'O seu salário teve um aumento de 10% e agora é {dez:.2f}')
else:
    quinze = s + s * 0.15
    print(f'O seu salário teve um aumento de 15% e agora é {quinze:.2f}')
