print('*'*30)
print('*  Analisador de Triângulos  *')
print('*'*30)

a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    print('Os seguimentos acima PODEM FORMAR triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo!')
