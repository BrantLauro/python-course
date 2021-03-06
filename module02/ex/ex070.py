total = products_1000 = 0
cheapest = ' '
prices = []
while True:
    print('~'*11)
    print('CHEAP STORE')
    print('~'*11)
    product = input('What is the product? ').strip()
    price = float(input('What is the price? $'))
    prices.append(price)
    total += price
    if min(prices) == price:
        cheapest = product
    if price >= 1000:
        products_1000 +=1
    choose = ' '
    while choose not in 'YN':
        choose = input('Want to continue? [Y/N] ').strip().upper()[0]
    if choose == 'N':
        break
print(f'The total is ${total:.2f}')
print(f'There is {products_1000} products more expansive than $1000.00')
print(f'The cheapest product is {cheapest} that costs: ${min(prices):.2f}')
