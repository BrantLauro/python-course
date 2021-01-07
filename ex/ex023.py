num = int(input('Digite um número entre 0 e 9999: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: {u} \n'
      f'Dezena: {d} \n'
      f'Centena: {c} \n'
      f'Milhar: {m}')
