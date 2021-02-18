num = int(input('Type a number between 0 and 9999: '))
u = num % 10
t = num // 10 % 10
h = num // 100 % 10
th = num // 1000 % 10

print(f'Unity: {u} \n'
      f'Ten: {t} \n'
      f'Hundred: {h} \n'
      f'Thousand: {th}')
