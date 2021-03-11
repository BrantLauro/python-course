product = 'Pencil', 1.75, 'Erase', 2.00, 'Notebook', 15.00, 'Pencil Case', 25.00, 'Protractor', 4.20, 'Compass', 9.99, 'Backpack', 120.00, 'Pens', 22.30, 'Book', 34.90
print('-'*40)
print(f"{'PRICES':^40}")
print('-'*40)
for pos in range(0, len(product)):
    if pos % 2 == 0:
        print(f'{product[pos]:.<30}', end='$')
    if pos % 2 == 1:
        print(f'{product[pos]:>7.2f}')
print('-'*40)
