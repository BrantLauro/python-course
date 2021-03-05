n = cont = 0
while True:
    n = int(input('Type a number: '))
    if n < 0:
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n*cont}')
        cont += 1
    cont = 0
