price = float(input('What is the price of the product? $'))
i = price - price * (10/100)
p = price + price * (10/100)

print(f'The product price is {price} \n'
      f'In cash will be {i} \n'
      f'Parceled out will be {p}')
